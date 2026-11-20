# Git hooks — Aksh Rana (URN 2581371)

## pre-commit

Checks every staged file for an unfinished-work marker. If one is
found, the commit is blocked and the file is named in the output.
A clean commit with no such marker passes.

## commit-msg

Checks the commit message: it must be at least 10 characters long
and start with `feat:`, `fix:`, `docs:`, `refactor:` or `chore:`.
A short message, or one with no prefix, is blocked.

## Sharing hooks

Hooks in `.git/hooks` are local only and are not sent by push or
received by clone. This project tracks its hooks in `.githooks/`
and each clone runs `git config core.hooksPath .githooks`.
