from contextlib import redirect_stdout
from hashlib import sha256
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Thread
import json
import unittest

from sync import synchronize


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.responses = {}
        responses = self.responses

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                response = responses.get(self.path)
                if response is None:
                    self.send_error(404)
                    return
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(response.encode())

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        self.base = f"http://127.0.0.1:{server.server_port}/docs/"
        self.config = {"base_url": self.base}
        self.responses.update({
            "/docs/llms.txt": "[Group](_llms/group.md)\n",
            "/docs/_llms/group.md": "[Page](../page.md)\n[Group](group.md)\n",
            "/docs/page.md": "# Updated page\n",
            "/docs/sitemap-only.md": "# Page missing from the index\n",
            "/docs/llms-full.txt": "# Combined documentation\n",
            "/docs/sitemap.xml": f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{self.base}page</loc></url><url><loc>{self.base}sitemap-only</loc></url></urlset>',
        })
        self.originals = {"page.md": b"# Old page\n", "obsolete.md": b"# Removed upstream\n", "INDEX.md": b"# Old index\n"}
        for relative, data in self.originals.items():
            (self.root / relative).write_bytes(data)
        self.manifest = json.dumps({"files": {relative: {"sha256": sha256(data).hexdigest()} for relative, data in self.originals.items()}}).encode()
        (self.root / "snapshot.json").write_bytes(self.manifest)
        (self.root / "README.md").write_text("Repository instructions\n")
        (self.root / "personal-note.md").write_text("An unmanaged file\n")

    def refresh(self):
        with redirect_stdout(StringIO()):
            return synchronize(self.root, self.config)

    def test_recursive_indexes_and_sitemap_union_update_only_managed_files(self):
        first = self.refresh()
        self.assertEqual((self.root / "page.md").read_text(), "# Updated page\n")
        self.assertTrue((self.root / "sitemap-only.md").is_file())
        self.assertFalse((self.root / "obsolete.md").exists())
        self.assertEqual((self.root / "README.md").read_text(), "Repository instructions\n")
        self.assertEqual((self.root / "personal-note.md").read_text(), "An unmanaged file\n")
        second = self.refresh()
        self.assertEqual(first["files"], second["files"])

    def test_failed_download_preserves_the_previous_snapshot(self):
        del self.responses["/docs/sitemap-only.md"]
        with self.assertRaises(OSError):
            self.refresh()
        for relative, data in self.originals.items():
            self.assertEqual((self.root / relative).read_bytes(), data)
        self.assertEqual((self.root / "snapshot.json").read_bytes(), self.manifest)
        self.assertFalse((self.root / "_llms").exists())

    def test_refresh_does_not_overwrite_unmanaged_files(self):
        self.responses["/docs/sitemap.xml"] = f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{self.base}personal-note</loc></url></urlset>'
        self.responses["/docs/personal-note.md"] = "# Upstream file with the same name\n"
        with self.assertRaisesRegex(ValueError, "Unmanaged file"):
            self.refresh()
        self.assertEqual((self.root / "personal-note.md").read_text(), "An unmanaged file\n")
        self.assertEqual((self.root / "snapshot.json").read_bytes(), self.manifest)

    def test_malformed_example_url_does_not_prevent_asset_download(self):
        image_url = self.base.removesuffix("docs/") + "image.svg"
        self.config["asset_hosts"] = ["127.0.0.1"]
        self.responses["/docs/page.md"] += f"\nExample: http://[host]\n![Image]({image_url})\n"
        self.responses["/image.svg"] = '<svg xmlns="http://www.w3.org/2000/svg"/>'
        snapshot = self.refresh()
        downloaded_assets = [record["url"] for relative, record in snapshot["files"].items() if relative.startswith("assets/")]
        self.assertEqual(downloaded_assets, [image_url])


if __name__ == "__main__":
    unittest.main()
