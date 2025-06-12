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

- Static files are just external files that you use in Django like images, JS, CSS, etc...
  
- ➜ Ensure `django.contrib.staticfiles` is included in your `INSTALLED_APPS`.

- ➜ In your `settings.py`, define `STATIC_URL`, for example:
    ```python
    STATIC_URL = "static/"
    ```

---

### 🔧 Why `STATICFILES_DIRS` is Important

`STATICFILES_DIRS` tells Django:

> “Hey, in addition to app-specific static folders, also check these extra directories for static files.”

#### ✅ When can you skip `STATICFILES_DIRS`?
You can omit it safely **only if**:

- You’re storing all your images, CSS, and JS inside an app’s `static/` folder.

📂 **Helpful Reference**:
- `movie.html`
- `views.py` (`movie_manager/movies`)
- `settings.py`
- `urls.py` (inside `movies` app)

---

## 📅 DAY 6

### ✅ Performing CRED Operations

#### 🧾 Handling Forms in Django


### 🔹 What's Going On Here?

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    Title : <input type="text" name="title" />
    year : <input type="text" name="year" />
    summary : <input type="text" name="summary" />
    <button type="submit">create</button>
</form>
```

* `<form method="post">`:
  Forms are how users send data to the server (like filling out a form on a website).
  `method="post"` means the browser will send the form data inside the **body** of the request, which is private.
  The alternative is `method="get"`, where data is **visible in the URL**.

* `enctype="multipart/form-data"`:
  This is used when you're uploading files (like images). It tells the browser to encode the form properly.
  Even though you’re not uploading files here, it's okay to include — or you can remove it if not needed.

* `{% csrf_token %}`:
  Django uses this for **security**.
  CSRF = Cross Site Request Forgery. This token ensures the form was submitted from your site and not by a hacker.
  If you forget this line, Django will block the form submission.

* `<input type="text" name="title" />`:
  This creates a text field.
  `name="title"` is the key you'll use to access this data in Django.

---

### 🔹 The Django View:

```python
def create(request):
    if request.POST:
        print(request.POST.get("title"))
        print(request.POST.get("year"))
        print(request.POST.get("summary"))

    return render(request, 'create.html')
```

---

### 🔹 What Does This Mean?

* **`request`**:
  This is an object Django gives you automatically.
  It contains everything about the current user’s request — method (GET or POST), data, user info, etc.

* **`if request.POST:`**
  Checks if the request has POST data (i.e., the user submitted the form).
  ✅ **Better practice**: Use `if request.method == "POST"` — it's more explicit and reliable.

* **`request.POST.get("title")`**:
  Gets the value the user typed into the `"title"` input.
  You use `.get()` so it doesn’t crash if the field is missing.

* **`render(request, 'create.html')`**:
  This renders the HTML template called `create.html`.
  Django sends the HTML page as a **response** back to the browser.
  Even after the form is submitted, we send back the same page — you can later change this to **redirect** or show a **success message**.

---  