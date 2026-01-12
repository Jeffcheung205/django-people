# Peoples Show Template

A Django project created during ERB lessons that displays student (not real) and people details.

## Project Description
This is a Django web application for managing and displaying people/student information.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Jeffcheung205/django-people.git
cd django-people
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Project Structure
```
django-people/
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── [Django apps and settings will be added here]
```

## Adding Your Local Project Files

If you have Django project files on your local computer that you want to add to this repository:

1. Navigate to your local django-people folder:
```bash
cd /path/to/your/document/django-people
```

2. Copy your Django project files to this repository (excluding virtual environments and cache files)

3. Stage all your project files:
```bash
git add .
```

4. Commit the changes:
```bash
git commit -m "Add Django project files"
```

5. Push to GitHub:
```bash
git push origin main
```

## Technologies Used
- Django 6.0
- Python 3.x
- SQLite (default database)

## Contributing
Feel free to submit issues and enhancement requests!
