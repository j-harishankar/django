# 📘 Django Learning Progress Tracker

---

## 📅 **DAY 1: Project Setup and Basics**

### ✅ Creating a Virtual Environment

```bash
python -m venv <env_name>
```

> Activate the environment (no path needed if VS Code is opened from the root directory).

### ✅ Installing Django and Dependencies

* Install Django and other required packages after activating the virtual environment.

---

## 🛠️ Creating a Django Project and App

### ▶️ Creating the Project

```bash
django-admin startproject <project_name>
```

* Creates a Django project with the same folder name.
* Multiple apps can exist within one project.

### ▶️ Creating an App

```bash
python manage.py startapp <app_name>
```

### ▶️ Running the Project

```bash
cd <project_name>
python manage.py runserver
```

---

## 📁 Important Django Files

### `views.py`

* Contains functions to handle HTTP requests and return responses.

### `settings.py`

* Main configuration file for:

  * Installed applications
  * Middleware
  * Templates
  * Database setup

### ⚠️ Tip: Always open VS Code from the root directory containing `manage.py`.

### 🔄 Django Request-Response Cycle

* A request hits the URL pattern.
* The mapped view function returns an HTTP response.

---

## ✅ Summary of Day 1

* Created a Django project and app
* Understood what an app is in Django
* Learned Django’s request-response cycle
* Explored basic Django file structure

---

## 📁 GitHub Commands

### ✨ Set Up Local Repo as GitHub Repo

```bash
git init
git remote add origin <http>
git add .
git commit -m "initial commit"
git push -u origin main
```

### ⚡ If a README already exists before pushing:

```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

---

## 📄 Django Templates

### ✨ About Templates

* Define the structure/layout of web pages
* Use plain HTML + Django Template Language (DTL)

### ✅ Steps to Use Templates

1. Create a template directory
2. Add path in `settings.py`
3. Create `.html` files
4. Write views to render templates
5. Map templates in `urls.py`

### 🌟 `render()` Function

```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

### ✨ Example HTML Syntax

```django
{% for item in dict %}
  {{ item }}
{% endfor %}
```

---

## 📅 DAY 3: URL Management Tips

* For cleaner code, define URLs inside individual apps (e.g., `movies.py`) instead of cramming everything into the main app's `urls.py`.

---

## ➜ Hyperlinks in Django

### Example:

```html
<ul>
  <li><a href="{% url 'create' %}">Create</a></li>
</ul>
```

* `<ul>` creates an unordered (bulleted) list.
* `<li>` defines each item.
* `<a>` is a hyperlink tag. `href` sets the URL.

---

## ➜ Include Tag

```django
{% include 'filename.html' %}
```

---

##  Template Inheritance

### ✨ Extending Templates

```django
{% extends 'base.html' %}
```

* Overriding content using blocks:

```django
{% block content %}
  {% include 'menu.html' %}
  <h1>Create</h1>
{% endblock %}
```

* Use when reusing common layouts like navbars but customizing the main content.
## 📅 DAY 5

### ✅ Steps to Use Templates

   * static files are just external files that you use in django like images,js,css etc...
    ➜ ensure django.contrib.staticfiles is included in your INSTALLED_APPS.
    ➜In your settings file, define STATIC_URL, for example:
    ``` 
        STATIC_URL = "static/"
    ```
   * 

    🔧 Why STATICFILES_DIRS is Important
    STATICFILES_DIRS tells Django:

    “Hey, in addition to app-specific static folders, also check these extra directories for static files.”
    ✅ When can you skip STATICFILES_DIRS?
    You can omit it safely only if:

    You’re storing all your images, CSS, JS inside an app’s static/ folder.
    checkout code of movie.html,views(movie_manager/movies),settings.py,urls.py(movies) for better understanding
---
