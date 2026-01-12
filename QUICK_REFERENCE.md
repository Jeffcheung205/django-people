# Quick Reference: Git Commands for This Project

## 📋 Quick Start - Push Your Local Django Files

```bash
# 1. Navigate to your local project folder
cd /path/to/your/document/django-people

# 2. Check what you're about to add
git status

# 3. Add all files
git add .

# 4. Commit with a message
git commit -m "Add Django project files"

# 5. Push to GitHub
git push origin main
```

## 🔍 Checking Status

```bash
# See what files have changed
git status

# See what changes you've made (before staging)
git diff

# See what changes are staged for commit
git diff --staged

# View commit history
git log --oneline
```

## ➕ Adding Files

```bash
# Add all files
git add .

# Add specific file
git add filename.py

# Add all files in a folder
git add foldername/

# Add all Python files
git add *.py
```

## 💾 Committing Changes

```bash
# Commit staged changes with message
git commit -m "Your commit message here"

# Add and commit in one step (for tracked files only)
git commit -am "Your message"
```

## 🚀 Pushing to GitHub

```bash
# Push to main branch
git push origin main

# Push to current branch
git push

# Push and set upstream (first time)
git push -u origin main
```

## 🔄 Pulling Updates

```bash
# Pull latest changes from GitHub
git pull origin main

# Fetch changes without merging
git fetch origin
```

## 🌿 Branch Management

```bash
# See all branches
git branch -a

# Create new branch
git checkout -b new-branch-name

# Switch to existing branch
git checkout branch-name

# Push branch to GitHub
git push origin branch-name
```

## ⚠️ Common Issues & Solutions

### Issue: Files are not being added
```bash
# Check if files are in .gitignore
cat .gitignore

# Force add a file that's ignored (use carefully!)
git add -f filename.py
```

### Issue: Wrong files were committed
```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Undo changes to a specific file (CAREFUL: this deletes changes!)
git checkout -- filename.py
```

### Issue: Need to see what's in .gitignore
```bash
# View .gitignore contents
cat .gitignore

# Check if a file is ignored
git check-ignore -v filename.py
```

### Issue: Remove file from Git but keep locally
```bash
# Remove from Git but keep local file
git rm --cached filename.py
git commit -m "Remove file from Git"
```

## 📝 Best Practices

1. **Before committing:** Always run `git status` to see what you're about to commit
2. **Write clear commit messages:** Describe what you changed and why
3. **Commit often:** Small, frequent commits are better than large ones
4. **Pull before push:** Always pull latest changes before pushing your work
5. **Don't commit:** Virtual environments, cache files, database files, or IDE settings

## 🆘 Need Help?

If something goes wrong:
```bash
# See the full log
git log

# See what you did recently
git reflog

# Get help on a command
git help <command>
# Example: git help commit
```

## 📚 Files in This Repository

- `README.md` - Main project documentation
- `SETUP_GUIDE.md` - Detailed setup instructions
- `QUICK_REFERENCE.md` - This file (quick Git command reference)
- `.gitignore` - Files that Git should ignore
- `requirements.txt` - Python dependencies

---

**Remember:** After following SETUP_GUIDE.md to add your Django project files, this repository will be ready for development!
