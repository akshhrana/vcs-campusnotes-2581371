# CampusNotes — VCS Assignment 2

**Student:** Aksh Rana
**URN:** 2581371
**Course:** Version Control System (CSE25303) — Assignment 2
**Repository:** https://github.com/akshhrana/vcs-campusnotes-2581371

A small Python CampusNotes demo used to practise remote repositories,
feature branches, pull requests, code review, Conventional Commits,
release tags, and Git hooks.

## Run

```bash
python3 campusnotes.py
python3 campusnotes.py search hooks
```

## Project files

- `campusnotes.py` — note list, display and search
- `notes.md` — sample study notes
- `docs/remote-setup.md` — remote, clone and pull steps
- `.githooks/` — shared pre-commit and commit-msg hooks

## Remote setup

```bash
git remote add origin https://github.com/akshhrana/vcs-campusnotes-2581371.git
git remote -v
git push -u origin main
```

See `docs/remote-setup.md` for the clone and pull steps.

## Git hooks

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit .githooks/commit-msg
```

The pre-commit hook rejects staged files with unfinished-work markers,
and the commit-msg hook enforces Conventional Commits messages of at
least 10 characters. Hooks live in `.git/hooks` locally and are not
shared by push; this project tracks them in `.githooks/` instead.
