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
## 📅 DAY 7

### ORM (Object Relational Mapping)

* ORM is an approach that uses object-oriented programming to manipulate the data in the relational database.
* Django ORM allows you to use the same Python API that interacts with various relational databases including MySQL, PostgreSQL, ORACLE...
* i.e., no need to write SQL queries; instead, write class-based models and the ORM will translate them into SQL queries.

### **`models.py`**

* Used to write classes for managing the data using classes.

* While creating a class, you shall inherit `Models` from Django's `models` module.

* After creating a model class, run:

```bash
python manage.py makemigrations
```

This creates a corresponding migration file, but the table won't be visible yet. It basically generates migration scripts.

* Now run:

```bash
python manage.py migrate
```

This will create the table in the database.

* You will notice several other tables created automatically — these are default features or tables provided by the Django framework.

---

### 🔧 `python manage.py makemigrations`

This command **creates new migration files** based on the changes you made to your models (in `models.py`).

#### Example:

If you add a new model like this:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Then run:

```bash
python manage.py makemigrations
```

📅 Django will create a migration file like:
`migrations/0001_initial.py`
This file contains Python code that describes how to create the `Student` table in your database.

> 💡 Think of this as Django **recording the changes** you want to make to the database.

---

### 🛠️ `python manage.py migrate`

This command **applies the migration files** to the actual database.

```bash
python manage.py migrate
```

📅 It creates or updates tables in the database according to the migrations.

> 💡 Think of this as **applying the recorded changes** to the real database.

---

### 🔁 Summary

| Command                           | Purpose                                               |
| --------------------------------- | ----------------------------------------------------- |
| `python manage.py makemigrations` | Detects changes in models and creates migration files |
| `python manage.py migrate`        | Applies the changes to the database                   |

---

* `id` is a primary key

---

### 📝 Storing Form Data in the Database in Django

Once you have:

* Created a **model** and applied **migrations**,
* And created a **form in your view**,

Then, instead of printing the submitted values to the terminal, you can **store them in the database**.

To do this, you need to:

1. Create an **object of the model class** (which represents the table).
2. Assign the form values to that object.
3. Save the object using `.save()`.

---

### ✅ Example

```python
from .models import MyModel

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        summary = request.POST.get("summary")

        # Create and save the object
        obj = MyModel(title=title, year=year, summary=summary)
        obj.save()

    return render(request, 'create.html')
```

This will save the submitted form data into the database table represented by `MyModel`.

Let me know if you want to use Django forms instead of manual `request.POST.get`.

---

* Note:

```python
from .models import MovieInfo
```

The `.` means: "import from the same package (i.e., the same app directory)."





### ✅ **Improved & Structured Version (with Explanation)**

```python
from django.shortcuts import render
from .models import MovieInfo  # Make sure you import your model

def cred(request):
    # Step 1: Fetch all movie records from the MovieInfo table
    all_movies = MovieInfo.objects.all()

    # Step 2: Print the queryset in the console (for debugging)
    print(all_movies)

    # Step 3: Pass the movies to the template using context
    return render(request, 'cred.html', {'movies': all_movies})
```

---

### 🧠 **Understanding `Model.objects.method()`**

In Django, you use this structure to interact with the database:

```
ModelName.objects.method()
```

* ✅ `ModelName` – Your model class (e.g., `MovieInfo`)
* ✅ `.objects` – The manager that allows database queries
* ✅ `.method()` – The query method (e.g., `all()`, `filter()`, `get()`, etc.)

---

### 🔍 Example in Plain English

> *“Give me all the records from the `MovieInfo` table.”*
> That’s what this line does:

```python
MovieInfo.objects.all()
```

---

### 📌 Summary Rule

> **Always access the database in Django using:**
> `Model.objects.method()`
> *(This keeps your code clean, predictable, and Djangoic.)*

---

Let me know if you want to also display these movies inside the `cred.html` template — I can guide you step by step.


* we have almost covered what is mvt architecture

## 📅 DAY 8



### django-admin interface

## 🧭 Why We Use Django `/admin` Interface

### 🔹 1. **Instant Dashboard for Managing Data**

* Add, edit, and delete records (like tasks, users, blog posts) **without writing code or SQL**.
* Acts as a built-in GUI for your database.

> 📌 Example: Want to test your `Task` model? Use `/admin` to add 5 tasks quickly instead of writing views or forms.

---

### 🔹 2. **Auto-generated & Customizable**

* Django auto-builds admin pages for your models.
* You can **customize filters, search fields, ordering, etc.**

---

### 🔹 3. **Saves Time in Early Development**

* Test your app logic **before** building full front-end UIs.

---

### 🔹 4. **Used by Real Projects Too**

* Many teams use Django admin for internal tools.
* You can **limit access to staff only**.

---

### ⚙️ How It Works (Conceptually)

1. Register your models in `admin.py`.
2. Django creates admin pages.
3. Login at `/admin` using a superuser account.
4. Manage all model data easily.

---



## 🧾 Why We Register Models in Django Admin


Registering a model in `admin.py` tells Django to **show it in the `/admin` panel**.

---

### 🔍 Without registering:

* Model exists in the database.
* But **won’t show up in the admin panel**.
* You **can’t manage its data visually**.

---

### 🧠 Think of it like this:

> "Django, I’ve created this model. Please include it in the admin panel so I can manage its data visually."

---

### 🔧 What registering does:

* Adds the model to the `/admin` sidebar.
* Enables **create/edit/delete** from admin UI.
* Allows testing data **without building frontend views**.
* Makes future customizations possible (search, filters, etc.).

---

### ✅ Summary

| Purpose                           | Result                                  |
| --------------------------------- | --------------------------------------- |
| Registering a model in `admin.py` | Model shows up in `/admin`              |
| Not registering it                | Admin dashboard won’t show that model   |
| Use case                          | Easy data management during development |

* eg: 
```from . models import MovieInfo
# Register your models here.
admin.site.register(MovieInfo)
```
### creating superuser :-

* python manage.py createsuperuser




### django shell 


### 🐚 What is the Django Shell?

The Django shell is an **interactive Python environment** that allows me to work directly with my Django project.  
I use it mainly for **testing and debugging**.

For example, I can **quickly create or retrieve database objects using my models**, without having to set up views or templates.  
This helps me verify that my **logic and database interactions** are working correctly.

---

### 🔧 Why is it useful?

It’s especially useful during development when I want to:

- ✅ Check if a query returns the correct results  
- ✅ Manually create or edit data  
- ✅ Test small pieces of logic without affecting the frontend

---

### 🚀 How do I open it?

```bash
python manage.py shell
````

This gives me **full access to my project’s models and settings**.
It’s like a **playground or lab** where I can safely test things without affecting the actual user interface.

---

### 💡 Bonus Example

If I have a `MovieInfo` model, I can do:

```python
from myapp.models import MovieInfo
MovieInfo.objects.create(title="Inception", director="Nolan", year=2010)
```
This creates a **movie record in the database instantly**, which I can then check in the **admin panel** or use in my **views**.


# 📄 Django ModelForm Guide

## 🧩 What is a ModelForm?

If you’re building a database-driven app, chances are you’ll have forms that map closely to Django models. For example, you might have a `BlogComment` model and want to create a form for users to submit comments.

In such cases, defining form fields again in a standard form is redundant, because the fields already exist in the model.

> **ModelForm** is a Django helper class that automatically generates a form based on your model.

##  Steps to Implement a ModelForm

### ✅ 1. Create `forms.py` in Your App Directory

Create a new file if it doesn't exist:

```
your_app/
├── models.py
├── views.py
├── forms.py  ← create this
```

### ✅ 2. Import Required Classes

In `forms.py`:

```python
from django.forms import ModelForm
from .models import YourModel  # Replace with your actual model
```

### ✅ 3. Create a Form Class

```python
class YourModelForm(ModelForm):
    class Meta:
        model = YourModel
        fields = '__all__'  # or specify fields like ['title', 'description']
```

### ✅ 4. Use Form in Your View

In `views.py`:

```python
from .forms import YourModelForm

def your_view(request):
    form = YourModelForm()
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'template.html', {'form': form})
```

### ✅ 5. Render Form in Your Template

In your `template.html`:

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

---


# Day-9

## ✏️ Edit / 🗑️ Delete Operations in Django

This guide explains how to implement **Edit** and **Delete** functionality in a Django app using primary keys in URLs.

---

## 📌 Steps for Edit & Delete Operations

### 1. ✅ Add Primary Key to URL

Update `urls.py` to pass the primary key (`pk`) through the URL:

```python
from . import views
from django.urls import path

urlpatterns = [
    path('edit/<pk>', views.edit, name='edit'),
    path('delete/<pk>', views.delete, name='delete'),
]
```

---

### 2. 🧠 Update Template to Pass Object ID

In your template (e.g., `cred.html`), add links for edit and delete, passing the `movieobj.id`:

```html
<td>
    <a href="{% url 'edit' movieobj.id %}">Edit</a> /
    <a href="{% url 'delete' movieobj.id %}">Delete</a>
</td>
```

---

## 🗑️ Delete Operation

### ✅ View (`views.py`)

```python
from django.shortcuts import render
from .models import MovieInfo

def delete(request, pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request, 'cred.html', {'movies': movie_set})
```

### 🔍 Explanation:

* `MovieInfo.objects.get(pk=pk)`: Retrieves the movie with the given primary key.
* `instance.delete()`: Deletes it from the database.
* `MovieInfo.objects.all()`: Fetches remaining movies.
* Renders the updated list in `cred.html`.

### 💡 Template Loop Example

```django
{% for movie in movies %}
    <p>{{ movie.title }}</p>
{% endfor %}
```

---

## ✏️ Edit Operation

### ✅ View (`views.py`)

```python
from django.shortcuts import render, redirect
from .models import MovieInfo

def edit(request, pk):
    instance = MovieInfo.objects.get(pk=pk)

    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        description = request.POST.get("description")

        instance.title = title
        instance.year = year
        instance.description = description
        instance.save()

        return redirect('some_view_name')  # Replace with your actual view name

    return render(request, 'edit.html', {'movie': instance})
```

### ✅ Template (`edit.html`)

```html
<form method="post">
    {% csrf_token %}
    <label>Title:</label>
    <input type="text" name="title" value="{{ movie.title }}"><br><br>

    <label>Year:</label>
    <input type="number" name="year" value="{{ movie.year }}"><br><br>

    <label>Description:</label>
    <textarea name="description">{{ movie.description }}</textarea><br><br>

    <button type="submit">Update</button>
</form>
```

---

## ✅ Summary

| Feature             | Action                                                |
| ------------------- | ----------------------------------------------------- |
| 🔗 Pass Primary Key | Through `<pk>` in URL                                 |
| 🗑️ Delete          | Retrieve instance → `.delete()`                       |
| ✏️ Edit             | Retrieve instance → update fields → `.save()`         |
| 🔁 Template         | Use `{% url 'edit' id %}` and `{% url 'delete' id %}` |



---

## ✏️ Edit Operation

### ✅ View (`views.py`)

```python
from django.shortcuts import render, redirect
from .models import MovieInfo

def edit(request, pk):
    instance = MovieInfo.objects.get(pk=pk)

    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        description = request.POST.get("description")

        instance.title = title
        instance.year = year
        instance.description = description
        instance.save()

        return redirect('some_view_name')  # Replace with your actual view name

    return render(request, 'edit.html', {'movie': instance})
```

### ✅ Template (`edit.html`)

```html
<form method="post">
    {% csrf_token %}
    <label>Title:</label>
    <input type="text" name="title" value="{{ movie.title }}"><br><br>

    <label>Year:</label>
    <input type="number" name="year" value="{{ movie.year }}"><br><br>

    <label>Description:</label>
    <textarea name="description">{{ movie.description }}</textarea><br><br>

    <button type="submit">Update</button>
</form>
```

---

## ✅ Summary

| Feature             | Action                                                |
| ------------------- | ----------------------------------------------------- |
| 🔗 Pass Primary Key | Through `<pk>` in URL                                 |
| 🗑️ Delete          | Retrieve instance → `.delete()`                       |
| ✏️ Edit             | Retrieve instance → update fields → `.save()`         |
| 🔁 Template         | Use `{% url 'edit' id %}` and `{% url 'delete' id %}` |



This will display all movies currently in the database.

---

### Summary Table

| Step           | Description                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------|
| URL Patterns   | Add `<pk>` to URLs for edit/delete, map to respective views                                      |
| Template Links | Use `{% url 'edit' obj.id %}` and `{% url 'delete' obj.id %}` in table rows                      |
| Delete View    | Retrieve by `pk`, delete, then render updated object list                                        |
| Template Loop  | Display all current objects using `{% for obj in objects %} ... {% endfor %}`                    |

---

**Tip:**  
Always use the object's primary key in the URL for edit and delete operations to uniquely identify which row to update or remove.



# ✅ Day-10: Connecting PostgreSQL to Django

---

## 📦 Step 1: Install PostgreSQL Adapter

Use `psycopg2` to connect Django with PostgreSQL:

```bash
pip install psycopg2
```

---

## 🗄️ Step 2: Create a PostgreSQL Database

Create a new database inside your PostgreSQL shell (e.g., `psql`) using:

```sql
CREATE DATABASE your_db_name;
```

You can leave most fields as default; you’ll use these details in `settings.py`.

---

## ⚙️ Step 3: Update Django `settings.py`

Modify the `DATABASES` setting:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Change from 'sqlite3'
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🔁 Step 4: Handle Existing Migrations

Since previous migrations were done with SQLite, you'll need to migrate again for PostgreSQL.

But if you want to **keep existing data**, follow the steps below.

---

## ✅ How to Move Data When Switching from SQLite to PostgreSQL

### **Option 1: Using `dumpdata` and `loaddata`**

This lets you migrate both schema and data safely.

1. **Export Data from SQLite:**

   ```bash
   python manage.py dumpdata > data.json
   ```

2. **Switch DB to PostgreSQL in `settings.py` (as shown above).**

3. **Run migrations for the new DB:**

   ```bash
   python manage.py migrate
   ```

4. **Load data into PostgreSQL:**

   ```bash
   python manage.py loaddata data.json
   ```

This ensures your old data is loaded into your new PostgreSQL tables.

---

## 🧠 Why This Works with Django

If we weren’t using Django, we would have to:

* Write raw SQL queries manually to recreate all tables and relationships.

But Django uses **ORM (Object Relational Mapping)**:

* So we just change the DB backend, run `migrate`, and the models are auto-converted into the correct DB structure.
* No need to rewrite queries!


### 📘 Django Media Handling – Easy Notes

#### 🔹 What’s the purpose?

To let users **upload files (like images)** and display them dynamically on your site (not just static images you added yourself).

---

### 🛠️ Setup Steps

#### ✅ 1. Add an `ImageField` or `FileField` in your model:

```python
poster = models.ImageField(upload_to='posters/')
```

> `upload_to` decides the folder inside your `media/` directory.

---

#### ✅ 2. Set up `MEDIA_URL` and `MEDIA_ROOT` in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

#### ✅ 3. Tell Django to serve media in `urls.py` (only during development):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### ⚠️ Common Gotchas

* Always run:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

  after adding new fields.

* In your template, check if file exists before showing:

  ```html
  {% if movie.poster %}
      <img src="{{ movie.poster.url }}" width="100">
  {% else %}
      No image uploaded
  {% endif %}
  ```

* Use `enctype="multipart/form-data"` in your form tag for file upload.




# ✅ Day-10: Learning ORM Relations in Django

## 🔗 One-to-One Relationship

### 📌 Concept:

* A **One-to-One relation** connects two models so that **each row in one model** is related to **exactly one row in another model**.
* In Django, this is achieved using `OneToOneField`.

### 🛠️ Steps:

1. **Create the related model first** (e.g., `CensorInfo`).
2. **Use that model as a field** in another model using `models.OneToOneField`.

### 🧠 Tip:

> When a new instance is created in the second model (e.g., `CensorInfo`), it can be linked to **only one** instance in the main model (e.g., `MovieInfo`).

---

## 🐚 Using the Django Shell Efficiently

### 🚫 Instead of:

* Writing views and running the server every time just to test data operations.

### ✅ Do this:

* Use the Django shell to interact with models directly. It’s faster for testing and learning.

### 💻 Example:

```python
>>> from movies.models import CensorInfo, MovieInfo

# Get an existing movie
>>> movie_obj = MovieInfo.objects.get(title='batman')

# Create a new CensorInfo and assign it to the movie
>>> movie_obj.censor = CensorInfo.objects.create(rating='a', certified_by='IMDB')

# Access the censor info
>>> movie_obj.censor
<CensorInfo: CensorInfo object (2)>

>>> print(movie_obj.censor)
CensorInfo object (2)

# Access a specific field
>>> movie_obj.censor.rating
'a'
```


```
chatgpt example:


>>> censor_obj = CensorInfo.objects.create(rating='A', certified_by='IMDB')

>>> movie1 = MovieInfo.objects.get(title='Batman')
>>> movie2 = MovieInfo.objects.get(title='Superman')

>>> movie1.censor = censor_obj
>>> movie2.censor = censor_obj   # ❗ This will override movie1's link


```