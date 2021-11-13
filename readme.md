# To Do List Readme

_This is a simple To Do List app, where you can create your own account, and create some tasks, view her description, update whenever you want all the fields or mark the task as completed. Also, you can delete any task if you want._

## Table of contents

- [Starting](#starting-)
- [Requeriments](#requeriments-)
- [Install and Run the project](#Install-and-Run-the-project-)
- [Deploy](#Deploy-)
- [Builded in](#Builded-in-)
- [Autor](#Autor-)

## Starting 🚀

_Fork the project to your profile, and then clone to your local machine._

```
git clone <repo-link>
git add .
git commit -m <"message">
git push origin master
```

### Requeriments 📋

_This project uses python 3.9.5, don't tested yet on other versions of python._
_Also, you need to have installed Postgresql to make database connection._

_To install all dependencies necessary to run the project on your local development environment you need to use pip to install requeriments.txt_

```
pip install -r .\requirements.txt
```

### Install and Run the project 🔧

_1.- Create your own database file._
_2.- To run the project, you have to create your own .env file to hidden your secret keys and DateBase connection, put debug=1 on local, or 0 if you want to deploy on production._

```
SECRET_KEY= <yoursecretkey>
DEBUG=1

DATABASE_NAME= <yourdatabase_name>
USER= <youruser>
PASSWORD= <yourpassword>
HOST= 127.0.0.1
DATABASE_PORT= 5432
```

_3.- Then you can migrate the models and make migrations._

```
python manage.py makemigrations
python manage.py migrate
```

_4. Finally, run server on your local machine._

```

python manage.py runserver
```

## Deploy 📦

_This project was deployment on heroku. You can see it here:_

- [To Do List](http://www.herokulink/)

## Builded in 🛠️

- [Django](http://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [HTML](https://)
- [CSS](http://)

## Autor ✒️

- **Marcelo De La Barrera** - [marcelodelabarrera](https://github.com/marcelodelabarrera)