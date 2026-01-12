# Setup Guide: How to Push Your Django Project Files

## Current Situation
You have a Django project in your computer at `document/django-people` that you want to push to this GitHub repository.

## Step-by-Step Instructions

### Option 1: If This is Your First Time Cloning the Repository

1. **Clone this repository to your computer:**
   ```bash
   git clone https://github.com/Jeffcheung205/django-people.git
   cd django-people
   ```

2. **Copy your Django project files:**
   - Copy all your Django project files from `document/django-people` to this cloned folder
   - **DO NOT copy these folders/files:**
     - `venv/` or `env/` (virtual environment)
     - `__pycache__/` folders
     - `.pyc` files
     - `db.sqlite3` (database file - optional, depends on your needs)
     - `.idea/` or `.vscode/` (IDE settings)

3. **Check what files will be added:**
   ```bash
   git status
   ```

4. **Add all your project files:**
   ```bash
   git add .
   ```

5. **Commit your changes:**
   ```bash
   git commit -m "Add Django project files from local computer"
   ```

6. **Push to GitHub:**
   ```bash
   git push origin main
   ```
   Or if you're on a different branch:
   ```bash
   git push origin your-branch-name
   ```

### Option 2: If You Already Have the Repository Cloned

1. **Navigate to your cloned repository:**
   ```bash
   cd /path/to/your/cloned/django-people
   ```

2. **Pull the latest changes:**
   ```bash
   git pull origin main
   ```

3. **Copy your project files** from `document/django-people` to this folder
   - Use File Explorer (Windows) or Finder (Mac) to copy files
   - Or use command line (replace the paths with your actual location):
   ```bash
   # On Windows (Command Prompt) - Replace with your actual path
   xcopy /E /I "C:\path\to\your\Documents\django-people\*" .
   
   # On Mac/Linux - Replace with your actual path
   cp -r ~/path/to/your/django-people/* .
   ```

4. **Check the status:**
   ```bash
   git status
   ```

5. **Add, commit, and push:**
   ```bash
   git add .
   git commit -m "Add Django project files"
   git push origin main
   ```

## What Files Should Be Included?

### ✅ Files to Include:
- `manage.py`
- All your Django app folders (e.g., `people/`, `students/`, etc.)
- `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
- Template files (`.html`)
- Static files (`.css`, `.js`, images)
- Requirements file (`requirements.txt`)
- README and documentation

### ❌ Files to Exclude (Already in .gitignore):
- Virtual environment folders (`venv/`, `env/`)
- Python cache (`__pycache__/`, `*.pyc`)
- Database file (`db.sqlite3`) - optional
- IDE settings (`.idea/`, `.vscode/`)
- Log files (`*.log`)
- Environment variables (`.env`)

## Troubleshooting

### Problem: "Permission denied" or "Authentication failed"
**Solution:** Make sure you're logged in to GitHub on your computer. You may need to set up SSH keys or use a personal access token.

### Problem: "Nothing to commit, working tree clean"
**Solution:** Your files might already be in the repository, or they're being ignored by `.gitignore`. Check `git status` to see what's happening.

### Problem: Files I want to include are being ignored
**Solution:** Check the `.gitignore` file and remove any patterns that are excluding your needed files.

### Problem: "src refspec main does not exist"
**Solution:** You might be on a different branch. Check your current branch with `git branch` and push to that branch, or switch to main with `git checkout main`.

## Need Help?

If you encounter any issues:
1. Check `git status` to see the current state
2. Check `git log` to see recent commits
3. Use `git diff` to see what changes you're about to commit
4. Feel free to create an issue in this repository for help

## Example Django Project Structure

After adding your files, your repository should look something like:
```
django-people/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── SETUP_GUIDE.md
├── people/                 # Your Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── django_people/          # Project settings folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── static/                 # Static files
    ├── css/
    ├── js/
    └── images/
```
