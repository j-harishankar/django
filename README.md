# django
track learning progress



-------------------------------------------DAY-1-----------------------------------------------------
                            CREATING VIRTUAL ENVIORNMENT
            python -m venv name
to activate
		just activate no path required since you already opened the vs code from the root directory  
            install all the required dependencies 
            
------------------------------CREATING A DJANGO PROJECT----------------------------------------

            django-admin startproject project_name [now we have created a framework or basic skeleton]
            ->there will be a folder with the same project name it is the first app that we created 
            ->there can be multiple apps inside a single project 
                            
                            CREATING AN APP 
            python manage.py startapp app_name


                            RUNNING A DJANGO PROJECT

            cd project_name
            python manage.py runserver


-------------------------------FILE DETAILS----------------------------------------------------
                        VIEWS.PY 
                            we write the functions here for response
                        SETTINGS.PY 
                            -> this is the main settings file of our django project 
                            -> this file is present for adding all installed applications 
                                as well as all the middleware application present 
                            -> it has information about templates,databases and other configurations 
                            
---------> IMPORTANT THING TO DO ALWAYS OPEN THE VSCODE FROM THE ROOT DIRECTORY WHICH CONTAINS MANAGE.PY<-------------------
an http request when called it will be forwarded to the function specified on the views for the corresponding response
 

summary: learned to create a Django application 
	 what is an app in Django 
	request response cycle of Django 
	file structure of Django 
		


-------------------------------GITHUB COMMANDS-------------------------------------------------
			TO SETUP A LOCAL REPO AS GITHUB REPO 
			
			git init 
			git remote add origin <http>
			git add .
 			git commit -m 
			git push -u origin main 
			

		if an readme file is present before pushing do
			git pull origin main --allow-unrelated-histories 
then 	
			git push origin main 
			

----------------------------------- DJANGO TEMPLATES-------------------------------------------

-->   django templates are the text files that define the structure and layout of the web page,allowing you to create dynamic HTML content.
--> They use a combination of plain HTML and Django Template Language(DTL).
-->after creating the template do mention the path on settings.py.
-->order create a template --> create html files --> create views for them --> describe it in urls.py --> describe path in settings.py

--------------------- render()--------------------------------------------------------
    render(request, template_name, context=None, content_type=None, status=None, using=None)
    request: The HTTP request object.

template_name: The path to your template file.

context: A dictionary containing the data you want to send to the template.
Purpose:
To generate a complete HTML response by rendering a template (HTML file) with dynamic data from your views.

Syntax in HTML 
            %for _ in dict%
            %endfor%

-----------------------------------Day 3-------------------------------------------------------
    --> its better to create the movies.py inside the app itself that is cosider you want to describe path of some functions created in movies insted of describing that on url.py file of main app which will eventually lead to unreadability of the code just create the url in specific file and describe from there itself for readability.


-----------------------------------------------------------------------------------------
    href(hyperlinks) :- automatically goes to the page instead of manually typing the url.
    <ul>
    <li><a href="{%url create%}">create</a></li>
    </ul>

    then initialize a name field inside url


    <ul></ul> is an HTML tag used to create an unordered list (bulleted list).

------------------------------------------------------------------------------------



<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

🔹 The <li> tags define the list items.
🔹 The bullets are shown by default.

<li></li> is an HTML tag used to define a list item inside <ul> (unordered list) or <ol> (ordered list).

 
--------------------------------------------------------------------------------------

<a></a> is an HTML tag used to create a hyperlink.

<a href="https://example.com">Visit Site</a>
href is the attribute that sets the link destination.

The text between <a> and </a> is the clickable part.

🔹 It opens a new page or website when clicked.


-----------------------------------------------------------------------------------------





