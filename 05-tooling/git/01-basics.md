# Git Basics
*Version control fundamentals*

## Core Concepts
*Key terms and mental model*

**Repository (repo)** – Project folder tracked by Git  
**Commit** – Snapshot of the tracked files at a point in time  
**Branch** – Lightweight pointer to a commit  
**Working directory** – Files on disk (untracked changes)  
**Staging area (index)** – Changes queued for the next commit  
**HEAD** – Pointer to the current branch/commit  
**Remote** – Copy of the repo hosted elsewhere (GitHub, GitLab)  

---

## Setup
*Configure identity and init*

```bash
git config --global user.name "Alice"
git config --global user.email "alice@example.com"
git config --global core.editor "code --wait"   # VS Code

git init                  # init repo in current dir
git clone https://...     # clone from remote
git remote -v             # list remotes
```

---

## Daily Workflow
*Stage, commit, push*

```bash
git status                # show working tree state
git diff                  # unstaged changes
git diff --staged         # staged changes

git add file.txt          # stage specific file
git add .                 # stage all changes
git add -p                # stage interactively (hunk by hunk)

git commit -m "feat: add user endpoint"
git commit --amend        # modify last commit (before push)

git push origin main      # push to remote
git pull origin main      # fetch + merge
git fetch origin          # fetch without merging
```

---

## Branching
*Create, switch, merge*

```bash
git branch                     # list local branches
git branch -a                  # include remote branches

git checkout -b feature/login  # create + switch
git switch -c feature/login    # modern syntax

git merge feature/login        # merge into current branch
git merge --no-ff feature/login  # always create merge commit

git branch -d feature/login    # delete merged branch
git branch -D feature/login    # force delete
git push origin --delete feature/login  # delete remote branch
```

---

## Undoing Changes
*Fix mistakes safely*

```bash
git restore file.txt           # discard unstaged changes
git restore --staged file.txt  # unstage file

git revert HEAD                # new commit that undoes last commit
git revert abc123              # undo specific commit

git reset --soft HEAD~1        # undo commit, keep staged
git reset --mixed HEAD~1       # undo commit, unstage (default)
git reset --hard HEAD~1        # undo commit, discard changes
```

**`revert`** – Safe; creates new undo commit (use on shared branches)  
**`reset`** – Rewrites history (only use on local/unshared commits)  

---

## Inspection
*Explore history*

```bash
git log                        # commit history
git log --oneline --graph      # compact visual graph
git log -p file.txt            # history with diffs for file

git show abc123                # show a specific commit
git blame file.txt             # line-by-line authorship

git stash                      # save dirty work temporarily
git stash pop                  # restore last stash
git stash list                 # all stashes
```
