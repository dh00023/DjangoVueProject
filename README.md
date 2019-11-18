# :bulb: New Brand Shop Project:bulb:

![Django](https://img.shields.io/badge/Django-v2.2.6-green)
![Pip](https://img.shields.io/badge/pypi-v19.3.1-blue)
![Vue](https://img.shields.io/badge/vue-3.11.0-green.svg)


## :building_construction: Installation

### Server

:rotating_light: Please, Install package of pip in virtual environment

Before launching the project, you have to install packages.

Install using `pip`


```
$ pip install -r server/requirements/development.txt
$ pip install -r server/requirements/production.txt
```

[:runner: install pip package manager and virtualenv package](./documents/setup-django.md)

### Client

🚨 Please, Install package of node.js

Before launching the project, you have to install packages.

Install using `npm`

```
$ npm install vue
```

[🏃 install package of node.js](./documents/setup-vuejs.md)

## :card_file_box:Data Migrations

### migrate

```
$ python ./manage.py makemigrations
```

If you want to see, SQL statements for migrations, you can use `sqlmigrate`

```
$ python ./manage.py sqlmigrate <app_name> <migration_number>
$ python ./manage.py sqlmigrate item 0001
```

If you want to automatically load initial data for an app, just call `manage.py loaddata <fixtures>`

```
$ python ./manage.py loaddata user/fixtures/data.json
$ python ./manage.py loaddata item/fixtures/data.json
$ python ./manage.py loaddata styleshare/fixtures/data.json
$ python ./manage.py loaddata magazie/fixtures/data.json
```

## :rocket: Launch

### Server

```
$ cd server
$ python manage.py runserver
```

### Client

```
$ cd client
$ npm install
$ npm run server
```

## Debug

```python
import pdb; pdb.set_trace()
```





https://jpadilla.github.io/django-rest-framework-jwt/
https://hjh5488.tistory.com/10