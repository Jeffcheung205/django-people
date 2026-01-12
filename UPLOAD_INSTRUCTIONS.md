# How to Upload Your Django Project Files to GitHub

Since you have your Django project files in your local `documents/django-people` folder, here's how to upload them to this repository:

## Option 1: Using Git Command Line (Recommended)

1. **Open Command Prompt or Terminal** and navigate to your Django project folder:
   ```bash
   cd C:\Users\YourUsername\Documents\django-people
   ```
   (Replace `YourUsername` with your actual Windows username)

2. **Initialize Git** (if not already initialized):
   ```bash
   git init
   ```

3. **Add the remote repository**:
   ```bash
   git remote add origin https://github.com/Jeffcheung205/django-people.git
   ```

4. **Pull the existing files** from the repository:
   ```bash
   git pull origin main --allow-unrelated-histories
   ```

5. **Add all your Django project files**:
   ```bash
   git add .
   ```

6. **Commit your changes**:
   ```bash
   git commit -m "Add Django project files from local D: drive"
   ```

7. **Push to GitHub**:
   ```bash
   git push origin main
   ```

## Option 2: Using GitHub Desktop (Easier for Beginners)

1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Sign in with your GitHub account
3. Click "File" → "Add Local Repository"
4. Browse to `C:\Users\YourUsername\Documents\django-people`
5. If it's not a Git repository, GitHub Desktop will offer to create one
6. Add the remote repository: `https://github.com/Jeffcheung205/django-people.git`
7. Click "Fetch origin" to get the latest changes
8. Review your changes in the left sidebar
9. Write a commit message (e.g., "Add Django project files")
10. Click "Commit to main"
11. Click "Push origin" to upload your files

## Option 3: Using Web Interface (For Small Number of Files)

1. Go to https://github.com/Jeffcheung205/django-people
2. Click "Add file" → "Upload files"
3. Drag and drop your Django project files or browse to select them
4. Write a commit message
5. Click "Commit changes"

**Note**: This method is not ideal for large projects with many files and folders.

## What Files to Upload

Make sure to upload your Django project files including:
- `manage.py`
- Project settings folder (e.g., `django_people/` or similar)
- Apps folders (e.g., `people/` or `students/`)
- Templates directory
- Static files directory
- Any other Python files, migrations, etc.

**Don't forget**: Add a `.gitignore` file to exclude:
- `__pycache__/` directories
- `*.pyc` files
- `db.sqlite3` (database file)
- Virtual environment folders (e.g., `venv/`, `env/`)
- `.env` files with sensitive data

## Need Help?

If you encounter any issues, please let me know:
- What error messages you see
- Which method you're trying to use
- Where you're getting stuck

Once you push your files, I'll be able to see them and help with any organization, fixes, or enhancements needed!
