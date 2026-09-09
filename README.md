# Cal.com documentation snapshot

A documentation mirror of [Cal.com's official documentation](https://cal.com/docs/).

Start with the [local documentation index](INDEX.md). The original [llms.txt](llms.txt), [combined export](llms-full.txt), and [sitemap](sitemap.xml) are also included.

Downloaded files retain their original paths and contents. Links and embedded components are preserved, so some references still require the upstream website or a compatible Markdown renderer. [snapshot.json](snapshot.json) records the latest sync time, source URLs, and file checksums.

Includes the API reference, developer guides, OpenAPI specification, standalone skill document, and referenced image assets.

## Use with skills

Skills use `~/.coloop-skills/docs/cal.com`. Clone this repository there when the directory is missing:

```sh
calcom_docs_root="${HOME}/.coloop-skills/docs/cal.com"
if [ ! -e "$calcom_docs_root" ]; then
  mkdir -p "${calcom_docs_root%/*}"
  git clone --depth 1 https://github.com/Genei-Ltd/calcom-docs.git "$calcom_docs_root"
fi
```

## Sync with the upstream documentation

Run from the repository root with Python 3.10 or newer on macOS or Linux. No additional packages are required.

```sh
python3 scripts/sync.py
```

The script follows nested documentation indexes, combines them with the sitemap, and downloads the current Markdown, OpenAPI, and image assets. It validates all downloads before updating the snapshot and removes files that are no longer in the upstream inventory. It stops if managed files have local changes or a download fails. Unmanaged files are preserved.

The script updates this checkout without committing or pushing. Maintainers can review the diff, commit, and push the refreshed snapshot. Existing skill caches can receive published updates with `git pull --ff-only` from a clean checkout, or run the sync script to fetch directly from Cal.com.

Run the sync integration checks with:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Original documentation and assets are by Cal.com and its contributors. This mirror adds no new license to the upstream content.
