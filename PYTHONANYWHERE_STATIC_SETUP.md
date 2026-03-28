# PythonAnywhere Static Files Setup Guide

## Current Configuration (✅ Correct)

Your `settings.py` is properly configured:
- `STATIC_URL = '/static/'`
- `STATICFILES_DIRS = [BASE_DIR / 'static']`
- `STATIC_ROOT = BASE_DIR / 'staticfiles'`
- `MEDIA_URL = '/media/'`
- `MEDIA_ROOT = BASE_DIR / 'media'`

Your templates correctly use:
- `{% load static %}`
- `{% static 'images/filename.png' %}`

## Steps to Fix on PythonAnywhere

### 1. Run Collectstatic (in PythonAnywhere Bash console)
```bash
cd /home/KylleAcibron/Kylle_Acibron
python manage.py collectstatic
# Type 'yes' when prompted
```

### 2. Configure Web Tab (Critical Step)

Go to **Web** tab in PythonAnywhere dashboard, find **Static Files** section, add:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/KylleAcibron/Kylle_Acibron/staticfiles` |
| `/media/` | `/home/KylleAcibron/Kylle_Acibron/media` |

### 3. Reload Web App

Click the **Reload** button on the Web tab.

### 4. Test Direct URLs

Open these in browser to verify:
- `https://KylleAcibron.pythonanywhere.com/static/images/default-profile.svg`
- `https://KylleAcibron.pythonanywhere.com/static/css/style.css`

## Quick Checklist

- [ ] Ran `python manage.py collectstatic` on PythonAnywhere
- [ ] Added `/static/` → `/home/KylleAcibron/Kylle_Acibron/staticfiles` in Web tab
- [ ] Added `/media/` → `/home/KylleAcibron/Kylle_Acibron/media` in Web tab (if using uploaded images)
- [ ] Reloaded the web app
- [ ] Tested direct image URLs

## Common Issues

| Problem | Solution |
|---------|----------|
| 404 on static files | Check Web tab static file mapping |
| 404 on media files | Add media URL mapping in Web tab |
| CSS not loading | Run collectstatic, check mapping |
| Images not showing | Verify files exist in static/images/ folder |

## Your Static Files Structure

```
Kylle_Acibron/
├── static/                 # Source static files (dev)
│   ├── css/style.css
│   ├── js/script.js
│   └── images/
│       ├── default-profile.svg
│       ├── default-project.svg
│       ├── HotelManagementSystem.png
│       ├── LMS.png
│       ├── VotingSystem.png
│       └── Profile.jpg
├── staticfiles/           # Collected static files (production)
├── media/                 # User-uploaded files
│   ├── profile/
│   └── projects/
└── portfolio/
    └── settings.py
```
