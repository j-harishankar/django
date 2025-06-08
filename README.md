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
