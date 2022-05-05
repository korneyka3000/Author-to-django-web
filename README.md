# Author-to-django-web
run commands in dj_client:
```
  pip install -r requirements.txt  
  python manage.py makemigrations  
  python manage.py migrate  
  python manage.py runserver  
``` 
run commands in dj_server:
```
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  docker build -t dj_server .
  docker run --rm -p 50051:50051 dj_server
```
