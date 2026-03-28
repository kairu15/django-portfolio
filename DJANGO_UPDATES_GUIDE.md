# Django Updates Guide: GitHub to PythonAnywhere
## Complete Workflow for Updating Deployed Applications

---

## 📋 Table of Contents

1. [Quick Update Workflow](#quick-update-workflow)
2. [Local Development Updates](#local-development-updates)
3. [Pushing Changes to GitHub](#pushing-changes-to-github)
4. [PythonAnywhere Update Process](#pythonanywhere-update-process)
5. [Database Migrations](#database-migrations)
6. [Static Files Updates](#static-files-updates)
7. [Advanced Update Scenarios](#advanced-update-scenarios)
8. [Troubleshooting Updates](#troubleshooting-updates)
9. [Automation & Best Practices](#automation--best-practices)
10. [Rollback Procedures](#rollback-procedures)

---

## ⚡ Quick Update Workflow

### For Simple Code Changes
```bash
# Local Development
git add .
git commit -m "Your update message"
git push origin main

# PythonAnywhere (Bash console)
cd ~/your-project-name
git pull origin main
# Reload web app in Web tab
```

### For Changes Requiring Updates
```bash
# Local Development
git add .
git commit -m "Update with dependencies/migrations"
git push origin main

# PythonAnywhere (Bash console)
cd ~/your-project-name
git pull origin main
workon your-project-env
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
# Reload web app in Web tab
```

---

## 💻 Local Development Updates

### 1. Make Your Changes
```bash
# Activate virtual environment
source venv/bin/activate  # Windows: venv\Scripts\activate

# Make code changes
# Edit files, add features, fix bugs, etc.
```

### 2. Test Locally
```bash
# Run development server
python manage.py runserver

# Test in browser: http://localhost:8000

# Run tests if you have them
python manage.py test
```

### 3. Check for New Dependencies
```bash
# If you installed new packages
pip install new-package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### 4. Check for Database Changes
```bash
# If you changed models
python manage.py makemigrations
python manage.py migrate

# Test migrations locally
python manage.py runserver
```

### 5. Update Static Files (if needed)
```bash
# If you added/changed CSS, JS, or images
# Collect static files locally to test
python manage.py collectstatic --noinput
```

---

## 🐙 Pushing Changes to GitHub

### 1. Check Git Status
```bash
git status
```

### 2. Stage Your Changes
```bash
# Add all changes
git add .

# Or add specific files
git add file1.py file2.html static/css/style.css
```

### 3. Review Changes
```bash
# See what will be committed
git diff --cached

# See commit history
git log --oneline -5
```

### 4. Commit Changes
```bash
# Good commit message format
git commit -m "feat: add user authentication system"
git commit -m "fix: resolve navigation menu bug"
git commit -m "update: improve homepage responsiveness"
git commit -m "docs: update README with deployment instructions"
```

### 5. Push to GitHub
```bash
# Push to main branch
git push origin main

# Push to specific branch
git push origin feature-branch-name

# Force push (use carefully)
git push origin main --force
```

### 6. Verify on GitHub
- Visit your repository on GitHub
- Check that your changes are visible
- Verify files are updated correctly

---

## 🌐 PythonAnywhere Update Process

### 1. Access PythonAnywhere Console
```bash
# Log into PythonAnywhere
# Open a Bash console
```

### 2. Navigate to Project Directory
```bash
# List your projects
ls
cd ~/your-project-name

# Verify current directory
pwd
```

### 3. Check Current Git Status
```bash
# Check if you have uncommitted changes
git status

# Check current branch
git branch

# Check if you're behind main
git log --oneline -5
```

### 4. Pull Latest Changes
```bash
# Simple pull (if no conflicts)
git pull origin main

# Or more explicit
git fetch origin
git merge origin/main
```

### 5. Handle Merge Conflicts (if any)
```bash
# If conflicts occur
git status
# Edit conflicted files
# Remove conflict markers
git add conflicted-file.py
git commit -m "Resolve merge conflicts"
```

### 6. Activate Virtual Environment
```bash
# Activate your project's virtual environment
workon your-project-env

# Or activate manually
source ~/.virtualenvs/your-project-env/bin/activate

# Verify activation
which python
pip list
```

---

## 🗄️ Database Migrations

### 1. Check for New Migrations
```bash
# See if there are pending migrations
python manage.py showmigrations

# Check for new migrations to apply
python manage.py migrate --dry-run
```

### 2. Apply Migrations
```bash
# Apply all pending migrations
python manage.py migrate

# Apply specific app migrations
python manage.py migrate appname

# Apply specific migration
python manage.py migrate appname 0001_initial
```

### 3. Create Migrations (if needed)
```bash
# If you changed models
python manage.py makemigrations

# Review generated migrations
git show HEAD:appname/migrations/000X_auto_*.py
```

### 4. Backup Before Major Migrations
```bash
# Backup SQLite database
cp db.sqlite3 db.sqlite3.backup.$(date +%Y%m%d)

# For PostgreSQL (paid tier)
pg_dump username$default > backup.sql
```

---

## 📁 Static Files Updates

### 1. Check Static Files Changes
```bash
# See if static files were updated
git diff HEAD~1 -- static/

# List static directory contents
ls -la static/
```

### 2. Collect Static Files
```bash
# Collect all static files
python manage.py collectstatic

# Collect without confirmation
python manage.py collectstatic --noinput

# Clear and recollect
rm -rf staticfiles/
python manage.py collectstatic --noinput
```

### 3. Verify Static Files
```bash
# Check staticfiles directory
ls -la staticfiles/

# Check specific files
ls -la staticfiles/css/
ls -la staticfiles/js/
ls -la staticfiles/images/
```

### 4. Test Static Files URLs
```bash
# Test in browser
# https://username.pythonanywhere.com/static/css/style.css
# https://username.pythonanywhere.com/static/js/script.js
```

---

## 🔧 Advanced Update Scenarios

### Scenario 1: New Python Dependencies
```bash
# Local
pip install new-package
pip freeze > requirements.txt
git add requirements.txt
git commit -m "add: new-package dependency"
git push origin main

# PythonAnywhere
git pull origin main
workon your-project-env
pip install -r requirements.txt
# Reload web app
```

### Scenario 2: Django Version Upgrade
```bash
# Local
pip install --upgrade Django==4.2.8
pip freeze > requirements.txt
# Test thoroughly
python manage.py runserver
python manage.py test
git commit -am "upgrade: Django to 4.2.8"
git push origin main

# PythonAnywhere
git pull origin main
workon your-project-env
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
# Reload web app
```

### Scenario 3: Environment Variables Changes
```bash
# Local - update .env
# Add new variables
git add .env
git commit -m "config: add new environment variables"
git push origin main

# PythonAnywhere
git pull origin main
# Update environment variables in .bashrc
echo "export NEW_VAR='value'" >> ~/.bashrc
source ~/.bashrc
# Reload web app
```

### Scenario 4: Database Schema Changes
```bash
# Local
# Modify models.py
python manage.py makemigrations
python manage.py migrate
python manage.py test
git add .
git commit -m "feat: update user model with new fields"
git push origin main

# PythonAnywhere
git pull origin main
workon your-project-env
# Backup database first
cp db.sqlite3 db.sqlite3.backup
python manage.py migrate
# Reload web app
```

---

## 🐛 Troubleshooting Updates

### Issue 1: Git Pull Fails
```bash
# Error: "Your local changes would be overwritten by merge"
git stash
git pull origin main
git stash pop

# Or commit local changes first
git add .
git commit -m "WIP: local changes"
git pull origin main
```

### Issue 2: Migration Conflicts
```bash
# Error: "Migration X depends on Y which is not applied"
python manage.py migrate --fake-initial

# Or reset migrations (advanced)
python manage.py migrate appname zero
python manage.py migrate appname
```

### Issue 3: Static Files Not Updating
```bash
# Clear static files completely
rm -rf staticfiles/
python manage.py collectstatic --noinput

# Check file permissions
chmod 755 staticfiles/
chmod 644 staticfiles/*/*
```

### Issue 4: Import Errors After Update
```bash
# Check installed packages
pip list

# Reinstall requirements
pip install -r requirements.txt --upgrade

# Check Python path
python -c "import sys; print(sys.path)"
```

### Issue 5: 500 Internal Server Error
```bash
# Check error logs in PythonAnywhere Web tab
# Look for recent error entries
# Common causes:
# - Syntax errors
# - Import errors
# - Database connection issues
# - Permission problems
```

---

## 🤖 Automation & Best Practices

### 1. Create Update Script
```bash
# Create update.sh in PythonAnywhere
nano ~/update.sh

#!/bin/bash
cd ~/your-project-name
echo "Starting update process..."
git pull origin main
source ~/.virtualenvs/your-project-env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
echo "Update completed. Reload web app manually."

# Make executable
chmod +x ~/update.sh
```

### 2. Use Git Hooks (Advanced)
```bash
# Create post-merge hook
nano .git/hooks/post-merge

#!/bin/bash
echo "Running post-merge tasks..."
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

### 3. Branch-Based Workflow
```bash
# Create feature branch
git checkout -b new-feature
# Make changes
git add .
git commit -m "feat: add new feature"
git push origin new-feature

# Merge to main when ready
git checkout main
git merge new-feature
git push origin main
```

### 4. Tagging Releases
```bash
# Tag release version
git tag -a v1.0.1 -m "Release version 1.0.1"
git push origin v1.0.1

# Deploy specific tag
git checkout v1.0.1
```

### 5. Pre-Deployment Checklist
```bash
# Create checklist script
echo "Pre-deployment checklist:"
echo "✓ Local tests passed?"
echo "✓ Requirements updated?"
echo "✓ Migrations tested?"
echo "✓ Static files tested?"
echo "✓ Environment variables set?"
echo "✓ Backup created?"
```

---

## 🔄 Rollback Procedures

### 1. Quick Rollback to Previous Commit
```bash
# Check commit history
git log --oneline -10

# Reset to previous commit
git reset --hard HEAD~1
git push origin main --force

# PythonAnywhere
git reset --hard HEAD~1
# Reload web app
```

### 2. Rollback Database
```bash
# Check migration history
python manage.py showmigrations

# Rollback specific migration
python manage.py migrate appname 0003_previous_migration

# Rollback all migrations
python manage.py migrate appname zero
```

### 3. Restore Database Backup
```bash
# SQLite restore
cp db.sqlite3.backup db.sqlite3

# PostgreSQL restore
psql username$default < backup.sql
```

### 4. Emergency Rollback Script
```bash
# Create rollback.sh
#!/bin/bash
cd ~/your-project-name
echo "Emergency rollback initiated..."
git reset --hard HEAD~1
source ~/.virtualenvs/your-project-env/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
echo "Rollback completed. Reload web app."
```

---

## 📝 Update Templates & Scripts

### 1. Simple Update Script
```bash
#!/bin/bash
# update.sh - Simple deployment script
PROJECT_DIR="$HOME/your-project-name"
VENV="$HOME/.virtualenvs/your-project-env"

cd "$PROJECT_DIR"
echo "Pulling latest changes..."
git pull origin main

echo "Activating virtual environment..."
source "$VENV/bin/activate"

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Update completed! Reload your web app in PythonAnywhere."
```

### 2. Comprehensive Update Script
```bash
#!/bin/bash
# comprehensive_update.sh - Full deployment with checks
PROJECT_DIR="$HOME/your-project-name"
VENV="$HOME/.virtualenvs/your-project-env"
BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)

echo "=== Django Update Script ==="
echo "Starting update at $(date)"

# Create backup
mkdir -p "$BACKUP_DIR"
if [ -f "$PROJECT_DIR/db.sqlite3" ]; then
    cp "$PROJECT_DIR/db.sqlite3" "$BACKUP_DIR/db.sqlite3.$DATE"
    echo "Database backed up"
fi

# Navigate to project
cd "$PROJECT_DIR"

# Check git status
if [ -n "$(git status --porcelain)" ]; then
    echo "WARNING: You have uncommitted changes!"
    echo "Stashing changes..."
    git stash
fi

# Pull latest changes
echo "Pulling latest changes..."
git pull origin main

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV/bin/activate"

# Update dependencies
echo "Updating dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run tests (if available)
if python manage.py test --verbosity=2; then
    echo "Tests passed!"
else
    echo "WARNING: Some tests failed"
fi

echo "Update completed successfully!"
echo "Remember to reload your web app in PythonAnywhere."
```

---

## 🎯 Quick Reference Commands

### Local Development
```bash
# Quick commit and push
git add . && git commit -m "update message" && git push origin main

# Update dependencies
pip install new-package && pip freeze > requirements.txt

# Create migrations
python manage.py makemigrations && python manage.py migrate
```

### PythonAnywhere Updates
```bash
# Standard update
cd ~/project && git pull && workon venv && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

# Quick update (no migrations/dependencies)
cd ~/project && git pull && python manage.py collectstatic --noinput
```

### Emergency Commands
```bash
# Quick rollback
git reset --hard HEAD~1 && git push --force

# Database backup
cp db.sqlite3 db.sqlite3.backup.$(date +%Y%m%d)

# Clear static files
rm -rf staticfiles/ && python manage.py collectstatic --noinput
```

---

## 📊 Update Workflow Summary

### Daily Updates (Code Only)
1. Make changes locally
2. `git add . && git commit -m "message" && git push`
3. PythonAnywhere: `git pull`
4. Reload web app

### Weekly Updates (With Dependencies)
1. Update dependencies locally
2. Test thoroughly
3. Commit and push
4. PythonAnywhere: Full update script
5. Reload web app

### Major Updates (Database/Models)
1. Create migrations locally
2. Test extensively
3. Backup production database
4. Deploy with migration
5. Verify functionality

---

## 🎉 Conclusion

This guide provides a complete workflow for updating Django applications from local development to PythonAnywhere deployment. 

**Key Points:**
- Always test locally before pushing
- Backup before major updates
- Use descriptive commit messages
- Monitor error logs after updates
- Have rollback procedures ready

**Remember:** Reload your web app in the PythonAnywhere Web tab after most updates to see changes take effect!

Happy updating! 🚀
