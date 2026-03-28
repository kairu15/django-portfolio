# Django to PythonAnywhere Deployment Guide
## Complete Workflow: Development → GitHub → PythonAnywhere

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Django Development Setup](#local-django-development-setup)
3. [Project Structure Best Practices](#project-structure-best-practices)
4. [Git & GitHub Setup](#git--github-setup)
5. [PythonAnywhere Account Setup](#pythonanywhere-account-setup)
6. [PythonAnywhere Deployment](#pythonanywhere-deployment)
7. [Static & Media Files Configuration](#static--media-files-configuration)
8. [Database Setup](#database-setup)
9. [Environment Variables & Security](#environment-variables--security)
10. [Common Issues & Troubleshooting](#common-issues--troubleshooting)
11. [Maintenance & Updates](#maintenance--updates)

---

## 🔧 Prerequisites

### Required Software
- **Python 3.8+** installed locally
- **Git** installed and configured
- **Code Editor** (VS Code, PyCharm, etc.)
- **Command Line/Terminal**

### Required Accounts
- **GitHub** account
- **PythonAnywhere** account (Free or Paid)

### Python Packages (install locally)
```bash
pip install django python-decouple whitenoise gunicorn
```

---

## 🏗️ Local Django Development Setup

### 1. Create New Django Project
```bash
# Navigate to your projects directory
cd ~/Documents/Projects

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Django and required packages
pip install django python-decouple whitenoise gunicorn

# Create Django project
django-admin startproject myproject .
```

### 2. Configure Settings
```python
# settings.py
import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=lambda v: [s.strip() for s in v.split(',')])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your apps here
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 3. Create Environment File
```bash
# .env (create this file in project root)
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Create Basic Project Structure
```bash
mkdir -p static/css static/js static/images
mkdir -p templates
mkdir -p media
touch static/css/style.css
touch static/js/script.js
touch templates/base.html
```

### 5. Initial Migration & Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📁 Project Structure Best Practices

```
myproject/
├── .env                    # Environment variables (don't commit)
├── .gitignore             # Git ignore file
├── manage.py
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── myproject/            # Django project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── static/               # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/            # HTML templates
├── media/               # User uploaded files
├── apps/                # Django apps (optional)
└── venv/               # Virtual environment (don't commit)
```

---

## 🐙 Git & GitHub Setup

### 1. Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial Django project setup"
```

### 2. Create .gitignore
```bash
touch .gitignore
```

### 3. Add to .gitignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/
staticfiles/

# Environment variables
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### 4. Create GitHub Repository
1. Go to [GitHub](https://github.com) and create new repository
2. Don't initialize with README, .gitignore, or license
3. Copy the repository URL

### 5. Connect Local to GitHub
```bash
git remote add origin https://github.com/username/repository-name.git
git branch -M main
git push -u origin main
```

### 6. Create requirements.txt
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt"
git push
```

---

## 🌐 PythonAnywhere Account Setup

### 1. Sign Up for PythonAnywhere
- Visit [PythonAnywhere](https://www.pythonanywhere.com)
- Choose Free tier (for testing) or Paid tier (for production)

### 2. Account Dashboard Overview
- **Consoles**: Terminal access
- **Files**: File manager
- **Web**: Web application configuration
- **Databases**: Database management

### 3. Create Virtual Environment
```bash
# In PythonAnywhere Bash console
mkvirtualenv --python=/usr/bin/python3.9 myproject-env
```

---

## 🚀 PythonAnywhere Deployment

### 1. Clone Your Repository
```bash
# In PythonAnywhere Bash console
cd ~
git clone https://github.com/username/repository-name.git
cd repository-name
```

### 2. Install Dependencies
```bash
# Activate virtual environment
workon myproject-env

# Install requirements
pip install -r requirements.txt
```

### 3. Configure Settings for Production
```python
# In PythonAnywhere, create production settings
# Add to settings.py
import os

# Production settings
if 'PYTHONANYWHERE' in os.environ:
    DEBUG = False
    ALLOWED_HOSTS = ['username.pythonanywhere.com']
    
    # Database configuration (SQLite for free tier)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic
# Type 'yes' when prompted
```

### 7. Configure Web Application
1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Manual Configuration**
4. Select **Python 3.9** (or latest)
5. Set **Source code**: `/home/username/repository-name`
6. Set **Working directory**: `/home/username/repository-name`
7. Set **WSGI configuration file**: `/home/username/repository-name/myproject/wsgi.py`

### 8. Edit WSGI Configuration
```python
# In the WSGI configuration file editor
import os
import sys

path = '/home/username/repository-name'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 9. Configure Virtual Environment
1. In **Web** tab, find **Virtualenv** section
2. Enter: `/home/username/.virtualenvs/myproject-env`
3. Click **OK**

### 10. Reload Web App
Click the **Reload** button in the Web tab

---

## 📁 Static & Media Files Configuration

### 1. Static Files Setup
```python
# settings.py (ensure these are configured)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 2. Configure Static Files in PythonAnywhere
1. Go to **Web** tab
2. Find **Static files** section
3. Add mapping:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/username/repository-name/staticfiles` |

### 3. Configure Media Files (if using)
1. Add mapping in **Static files** section:

| URL | Directory |
|-----|-----------|
| `/media/` | `/home/username/repository-name/media` |

### 4. Test Static Files
Visit: `https://username.pythonanywhere.com/static/css/style.css`

---

## 🗄️ Database Setup

### 1. SQLite (Free Tier - Default)
```python
# Already configured in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 2. PostgreSQL (Paid Tier - Recommended)
```bash
# In PythonAnywhere Databases tab
# Create PostgreSQL database
# Note connection details
```

```python
# Update settings.py for PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'username$default',
        'USER': 'username',
        'PASSWORD': 'your-database-password',
        'HOST': 'username.postgres.pythonanywhere-services.com',
        'PORT': '5432',
    }
}
```

```bash
# Install PostgreSQL adapter
pip install psycopg2-binary
```

---

## 🔒 Environment Variables & Security

### 1. Secure Your Settings
```python
# settings.py
from decouple import config

# Use environment variables
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=lambda v: [s.strip() for s in v.split(',')])
```

### 2. Set Environment Variables in PythonAnywhere
```bash
# In PythonAnywhere Bash console
echo "export SECRET_KEY='your-production-secret-key'" >> ~/.bashrc
echo "export DEBUG=False" >> ~/.bashrc
echo "export ALLOWED_HOSTS='username.pythonanywhere.com'" >> ~/.bashrc
source ~/.bashrc
```

### 3. Security Best Practices
- Never commit `.env` file
- Use strong `SECRET_KEY`
- Set `DEBUG = False` in production
- Use HTTPS (PythonAnywhere provides this)
- Regularly update dependencies

---

## 🐛 Common Issues & Troubleshooting

### 1. Static Files Not Loading
**Problem**: 404 errors for CSS/JS/images
**Solution**:
```bash
# Run collectstatic
python manage.py collectstatic

# Check Web tab static file mappings
# URL: /static/
# Directory: /home/username/repository-name/staticfiles

# Reload web app
```

### 2. Database Error
**Problem**: "no such table" or database connection errors
**Solution**:
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 3. 500 Internal Server Error
**Problem**: Server error, blank page
**Solution**:
```bash
# Check error logs in Web tab
# Check Django settings
# Verify virtual environment is activated
```

### 4. Import Error
**Problem**: Module not found
**Solution**:
```bash
# Install missing packages
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### 5. Permission Denied
**Problem**: File permission errors
**Solution**:
```bash
# Fix file permissions
chmod 755 /home/username/repository-name
```

---

## 🔄 Maintenance & Updates

### 1. Updating Your Application
```bash
# Pull latest changes
git pull origin main

# Install new dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Reload web app (in PythonAnywhere Web tab)
```

### 2. Backup Database (SQLite)
```bash
# Backup SQLite database
cp db.sqlite3 db.sqlite3.backup
```

### 3. Monitor Logs
- Check **Web** tab for error logs
- Monitor **Consoles** for application logs
- Set up email notifications for critical errors

### 4. Performance Optimization
- Use Django Debug Toolbar in development
- Optimize database queries
- Use caching for frequently accessed data
- Compress static files

---

## 📚 Quick Reference Commands

### Local Development
```bash
# Start project
django-admin startproject myproject .
python manage.py startapp myapp

# Development server
python manage.py runserver

# Database operations
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Static files
python manage.py collectstatic
```

### Git Commands
```bash
# Stage and commit
git add .
git commit -m "Your commit message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main
```

### PythonAnywhere Commands
```bash
# Virtual environment
mkvirtualenv myproject-env
workon myproject-env
deactivate

# Install dependencies
pip install -r requirements.txt
pip freeze > requirements.txt

# Django operations
python manage.py migrate
python manage.py collectstatic
```

---

## 🎯 Deployment Checklist

### Pre-Deployment
- [ ] Local testing complete
- [ ] `DEBUG = False` in production settings
- [ ] `ALLOWED_HOSTS` configured
- [ ] All secrets in environment variables
- [ ] `requirements.txt` updated
- [ ] Static files organized
- [ ] Database migrations ready

### PythonAnywhere Setup
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Database configured
- [ ] Static files collected
- [ ] Web app configured
- [ ] WSGI file updated
- [ ] Static files mapped
- [ ] Web app reloaded

### Post-Deployment
- [ ] Website loads correctly
- [ ] Static files working
- [ ] Database operations working
- [ ] Admin panel accessible
- [ ] Error logs checked
- [ ] HTTPS working

---

## 📞 Support & Resources

### Official Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [PythonAnywhere Help](https://help.pythonanywhere.com/)
- [Git Documentation](https://git-scm.com/doc)

### Community Forums
- [Stack Overflow](https://stackoverflow.com/)
- [Django Forum](https://forum.djangoproject.com/)
- [PythonAnywhere Forum](https://www.pythonanywhere.com/forums/)

### Common Tools
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)
- [Whitenoise](https://whitenoise.evans.io/)
- [Gunicorn](https://gunicorn.org/)
- [Python Decouple](https://github.com/henriquebastos/python-decouple)

---

## 🎉 Congratulations!

You now have a complete Django application deployed on PythonAnywhere! 

**Next Steps:**
1. Set up custom domain (if you have one)
2. Configure email services
3. Set up monitoring and logging
4. Add SSL certificate (PythonAnywhere provides this)
5. Consider CI/CD pipeline for automated deployments

**Remember:** Keep your dependencies updated, regularly backup your data, and monitor your application for issues.

Happy coding! 🚀
