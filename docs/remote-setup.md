# Remote setup — Aksh Rana (URN 2581371)

Repository: https://github.com/akshhrana/vcs-campusnotes-2581371

```bash
git remote add origin https://github.com/akshhrana/vcs-campusnotes-2581371.git
git remote -v
git push -u origin main
git clone https://github.com/akshhrana/vcs-campusnotes-2581371.git campusnotes-clone
cd campusnotes-clone
git pull
```

Branches use upstream tracking (`git push -u origin <branch>`), so later
pushes and pulls need no extra arguments. The clone in a second folder
proves the remote copy is complete and can be pulled back.
