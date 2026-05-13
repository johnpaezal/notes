# Git Workflows
*Branching strategies and team collaboration*

## Git Flow
*Feature-branch model for releases*

```
main          ──────────────────────●─────────────── (production)
                                   /
release/1.0  ───────────────●─────●
                           /
develop      ──────●───────────●───────────── (integration)
                  / \         /
feature/A   ─────   ──────────
```

**`main`** – Production-ready code only  
**`develop`** – Integration branch for features  
**`feature/*`** – One branch per feature, merged into develop  
**`release/*`** – Prep for release; only bugfixes allowed  
**`hotfix/*`** – Emergency fixes branched from main  

---

## GitHub Flow
*Simplified: main is always deployable*

```
main     ──────────────────────────●───────────
                                  /
feature  ──────────────●─────────●
                      PR merged
```

1. Branch from `main`
2. Commit + push
3. Open Pull Request
4. Review + CI passes
5. Merge to `main`
6. Deploy immediately

Best for: continuous delivery, small teams.

---

## Rebase vs Merge
*Two ways to integrate branches*

```bash
# Merge — preserves branch history, creates merge commit
git checkout main
git merge feature/login

# Rebase — rewrites commits on top of main, linear history
git checkout feature/login
git rebase main
# then fast-forward merge
git checkout main
git merge feature/login
```

**Use merge**: shared/public branches, preserving full history  
**Use rebase**: local feature branches to keep history clean  
**Never rebase**: commits already pushed to shared remotes  

---

## Resolving Conflicts
*When two branches modify the same code*

```bash
git merge feature/login
# CONFLICT (content): Merge conflict in users.py

# File shows:
# <<<<<<< HEAD
# current branch code
# =======
# incoming branch code
# >>>>>>> feature/login

# 1. Edit file to keep correct version
# 2. Stage the resolved file
git add users.py
# 3. Complete the merge
git commit
```

---

## Conventional Commits
*Standardized commit message format*

```
<type>(<scope>): <short description>

feat(auth): add JWT login endpoint
fix(users): handle null email in create
docs(readme): update setup instructions
refactor(db): extract session factory
test(auth): add token expiry tests
chore(deps): upgrade FastAPI to 0.104
```

**Types**: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `perf`

---

## Useful Commands
*Less common but handy*

```bash
# Interactive rebase: squash, reorder, edit commits
git rebase -i HEAD~3

# Cherry-pick a commit from another branch
git cherry-pick abc123

# Find commit that introduced a bug (binary search)
git bisect start
git bisect bad                  # current is broken
git bisect good v1.0            # last known good

# Clean untracked files
git clean -fd                   # remove untracked files+dirs
git clean -n                    # dry run (preview)
```
