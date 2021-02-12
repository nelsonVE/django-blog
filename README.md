# Django blog
A simple blog made with django and bootstrap 5.0
### Installation

This project has been made in python 3.6.0
To install, first clone the repository and then install the dependecies
```sh
$ pip install -r requirements/local.txt
```

Then, you need to run the migrations to setup the database
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Doesn't forget to create a superuser!
```sh
$ python manage.py createsuperuser
```

And then just run the server
```sh
$ python manage.py runserver
```

### Dependencies

| Dependency | Version |
| ------ | ------ |
| asgiref | 3.3.1 |
| Django | 3.1.6 |
| pytz | 2021.1 |
| sqlparse | 0.4.1 |
