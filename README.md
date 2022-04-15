 django2_blog:
a blog publishing website based on Django 2 . 

the install guide:
1. create virtual env for it  
   #cd django2_blog
   #virtualenv env --python=python3.8
2. install django
   #pip install django==2.0
   #pip list
   there will show the installed packages:
    Package    Version
    ---------- -------
    Django     2.0
    pip        20.2.3
    pytz       2022.1
    setuptools 50.3.0
    wheel      0.35.1

3. migrate
   #python manage.py makemigrations
   #python manage.py migrate
   will create db.sqlite3 in current directory.
   
4. run server
   #python  manage.py runserver 
   it shows:
     Django version 2.0, using settings 'django2_blog.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.
 
