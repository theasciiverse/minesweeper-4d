# Changes from upstream

This is the Asciiverse packaging of [minesweeper_4d](https://github.com/itabesamesa/minesweeper_4d_rs)
by itabesamesa (MIT), built from upstream's main as of `c9480ee` (25
January 2026, version 0.1.17 as published on crates.io; upstream has no
tags). Upstream is the `upstream` remote; the `asciiverse` branch carries
the changes below.

## Code

- **Starts without a config file, wherever it is started from.** The game
  panicked unless `config.toml` had been copied by hand into its config
  folder, and it named that folder after `argv[0]`, so started by its full
  path (as av and the system packages do) it looked in the wrong place.
  The default `config.toml` is now built into the binary, with the user's
  own file (or `--config`) layered over it key by key, in a folder named
  `minesweeper_4d` however the game is started. Worth offering upstream.

## Packaging (new files)

- `.github/workflows/release.yml`: av archives for Linux (static), macOS
  and Windows, each x86-64 and ARM64, plus SHA256SUMS, and .deb, .rpm,
  .apk and Arch packages. Each archive also carries the default
  `config.toml`, to copy and edit.
- `asciiverse/nfpm.yaml`: the system packages. The package is called
  `minesweeper-4d`; the command stays `minesweeper_4d`.
- `asciiverse/record-preview.py`: records the catalog preview (seed 42,
  the cursor walking all four axes, then free cells uncovered one by one).

## Ours

- **How to play it, at the top of README.md.** A short note on installing
  and starting it with av; the original text follows unchanged.
