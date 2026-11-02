#!/usr/bin/env python3
"""Records asciiverse/minesweeper-4d.cast, the catalog preview, at 100x30
(hub/RECORDING.md): a game on the default 4x4x4x4 field with seed 42.
The cursor walks along all four axes, so the highlighted neighbourhood
shows how far a cell reaches in 4D, then F (find a free cell) and Space
uncover the field cell by cell, with a few flags. Uses only the built-in
config, so a config.toml of your own does not change the recording.
Usage, from the repo root with a release build:
python3 asciiverse/record-preview.py [binary]"""
import os, pty, struct, fcntl, select, sys, termios, time, tempfile

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
binary = sys.argv[1] if len(sys.argv) > 1 else f"{root}/target/release/minesweeper_4d"
cfg = tempfile.mkdtemp()
env = dict(os.environ, TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8",
           XDG_CONFIG_HOME=cfg, HOME=cfg)
cmd = f"{binary} -s 42 -r f"

keys = [(2.0, b" ")]
# walk the cursor through x, y, z and w and back
for k in b"lllkjjjddaawwss":
    keys.append((0.35, bytes([k])))
# uncover free cells, looking around now and then
for i in range(26):
    keys.append((0.45, b"f"))
    keys.append((0.35, b" "))
    if i % 6 == 5:
        for k in b"dwal":
            keys.append((0.3, bytes([k])))
keys += [(3.0, b"q"), (1.0, b"")]

pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", cmd,
        f"{root}/asciiverse/minesweeper-4d.cast"], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))
for wait, key in keys:
    end = time.time() + wait
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.03)
        if r:
            try: os.read(fd, 65536)
            except OSError: break
    if key: os.write(fd, key)
for _ in range(50):
    if os.waitpid(pid, os.WNOHANG)[0]: break
    time.sleep(0.2)
