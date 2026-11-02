# 4D Minesweeper (Asciiverse packaging)

Minesweeper in four dimensions, by itabesamesa, in Rust and Ratatui;
packaged for the Asciiverse catalog and as system packages. Not our code:
keep changes small, list every one in PATCHES.md, and offer fixes upstream.

- Remotes: `upstream` is github.com/itabesamesa/minesweeper_4d_rs,
  `origin` is github.com/theasciiverse/minesweeper-4d.
- Branch `asciiverse` = upstream main plus our commits.
- Catalog id `minesweeper-4d`; binary and config folder `minesweeper_4d`
  (upstream's crate name, kept).
- Release: tag `v<version>-av.<n>` and push it.
- Local static build: `docker run --rm -v "$PWD":/src -w /src
  rust:1-alpine sh -c 'apk add musl-dev && cargo build --release'`.
- Layout: the default 4x4x4x4 field with the info box needs 94x21; the
  field is drawn as background colour, two columns per cell, so a plain
  `tmux capture-pane -p` shows it blank (use `-e`).
- Settings: the built-in `config.toml`, overridden by
  `$XDG_CONFIG_HOME/minesweeper_4d/config.toml`. Ctrl+O saves a game to
  the Downloads folder (`-o` changes it).
