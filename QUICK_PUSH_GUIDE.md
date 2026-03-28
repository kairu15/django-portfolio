# Push Updated Code to PythonAnywhere
## Quick Step-by-Step Guide

---

## 🚀 Two-Step Process

### STEP 1: Push Code to GitHub (On Your Computer)

```bash
# 1. Open terminal in your project folder
cd C:\Users\kylle\OneDrive\Desktop\Kylle_Acibron

# 2. Check what files changed
git status

# 3. Add all changes to git
git add .

# 4. Commit with a message describing your changes
git commit -m "update: fixed homepage layout and added new project"

# 5. Push to GitHub
git push origin main
```

**✅ Done! Your code is now on GitHub.**

---

### STEP 2: Pull Code to PythonAnywhere (In PythonAnywhere Console)

```bash
# 1. Open PythonAnywhere dashboard
# 2. Click "Consoles" tab
# 3. Click "Bash" to open a terminal

# 4. Navigate to your project
cd ~/Kylle_Acibron

# 5. Get the latest code from GitHub
git pull origin main

# 6. (ONLY IF you installed new packages)
workon Kylle_Acibron-venv
pip install -r requirements.txt

# 7. (ONLY IF you changed database models)
python manage.py migrate

# 8. (ALWAYS DO THIS for code changes)
python manage.py collectstatic
# Type 'yes' when prompted
```

**✅ Done! Code updated on server.**

---

### STEP 3: Reload Your Web App

```
# 1. Go to PythonAnywhere "Web" tab
# 2. Click the GREEN "Reload" button
# 3. Wait 10-15 seconds
```

**✅ Your website is now updated!**

---

## 📋 Quick Reference Card

### Simple Code Changes (HTML, CSS, Python views)
```bash
# Local computer
git add . && git commit -m "your message" && git push origin main

# PythonAnywhere console
cd ~/Kylle_Acibron && git pull origin main && python manage.py collectstatic

# Then: Click Reload in Web tab
```

### Code + New Packages
```bash
# Local computer
git add . && git commit -m "your message" && git push origin main

# PythonAnywhere console
cd ~/Kylle_Acibron && git pull origin main && workon Kylle_Acibron-venv && pip install -r requirements.txt && python manage.py collectstatic

# Then: Click Reload in Web tab
```

### Code + Database Changes
```bash
# Local computer
git add . && git commit -m "your message" && git push origin main

# PythonAnywhere console
cd ~/Kylle_Acibron && git pull origin main && workon Kylle_Acibron-venv && python manage.py migrate && python manage.py collectstatic

# Then: Click Reload in Web tab
```

---

## 🎯 Visual Workflow

```
[Your Computer]                    [PythonAnywhere]
     |                                  |
     | 1. Make code changes             |
     | 2. git add .                     |
     | 3. git commit -m "message"       |
     | 4. git push origin main          |
     |-----------> [GitHub] <-----------|
     |                                  |
     |                      5. git pull origin main
     |                      6. python manage.py collectstatic
     |                      7. Click Reload button
     |                                  |
     v                                  v
   Code Updated!                    Website Live!
```

---

## ⚠️ Common Mistakes to Avoid

| ❌ Wrong | ✅ Right |
|---------|---------|
| Forget to commit | Always `git commit` before push |
| Forget to push | `git push origin main` sends to GitHub |
| Forget collectstatic | Always run after pulling code |
| Forget to reload | Click Reload in Web tab |
| Skip virtual environment | Use `workon Kylle_Acibron-venv` for pip installs |

---

## 🔧 Troubleshooting

### "git pull" says "Already up to date"
- You forgot to push from local computer
- Run: `git push origin main` on your computer first

### "Module not found" error
- New package not installed on PythonAnywhere
- Run: `workon Kylle_Acibron-venv && pip install -r requirements.txt`

### Static files not showing
- Forgot to run collectstatic
- Run: `python manage.py collectstatic`

### Website not updated
- Forgot to click Reload button
- Go to Web tab and click Reload

### Database error
- New migrations not applied
- Run: `python manage.py migrate`

---

## 📝 Example Session

### Local Computer (VS Code Terminal):
```
$ git status
Changes not staged for commit:
  modified:   templates/core/home.html
  modified:   static/css/style.css

$ git add .
$ git commit -m "fix: improve homepage styling"
$ git push origin main

Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.2 KiB | 1.2 MiB/s, done.
To https://github.com/username/Kylle_Acibron.git
   a1b2c3d..e4f5g6h  main -> main
```

### PythonAnywhere (Bash Console):
```
$ cd ~/Kylle_Acibron
$ git pull origin main

From https://github.com/username/Kylle_Acibron
 * branch            main       -> FETCH_HEAD
Updating a1b2c3d..e4f5g6h
 templates/core/home.html   | 15 +++++++++++++++
 static/css/style.css       | 24 ++++++++++++++++++++++++
 2 files changed, 39 insertions(+)

$ python manage.py collectstatic

132 static files copied to '/home/username/Kylle_Acibron/staticfiles'.

# Then go to Web tab and click Reload
```

---

## 🎉 Success Checklist

After updating, verify:
- [ ] Changes show on your website
- [ ] No 500 errors in browser
- [ ] Static files (CSS/images) load correctly
- [ ] No errors in error log (Web tab)

**Website URL:** `https://KylleAcibron.pythonanywhere.com`

---

## 💡 Pro Tips

1. **Test locally first** - Always run `python manage.py runserver` before pushing
2. **Small commits** - Commit often with clear messages
3. **Check status** - Use `git status` to see what's changed
4. **Backup** - For big changes, backup database first
5. **Reload** - Always click Reload after updates

**Remember:** Code changes → GitHub → PythonAnywhere → Reload → Live!
