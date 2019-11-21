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

[:runner: Install pip package manager and virtualenv package](./documents/setup-django.md)

### Client

🚨 Please, Install package of node.js

Before launching the project, you have to install packages.

Install using `npm`

```
$ npm install vue
```

[🏃 Install package of node.js](./documents/setup-vuejs.md)


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

## Create App

To create your app, make sure you’re in the same directory as `manage.py` and type this command.

```
$ django-admin startapp <app_name>
```

- `config/settings/base.py` : You have to add your app config to INSTALLED_APPS

```python

INSTALLED_APPS = [
 	...
    # project apps
    'magazine.apps.MagazineConfig',
    'styleshare.apps.StyleshareConfig',
    'item.apps.ItemConfig',
    'user.apps.UserConfig',
    # your app config
]
```

## :floppy_disk:Database

### create table

```python
# app/models.py
from django.db import models
class ModelName(models.Model):
	title = models.CharField("제목", max_length=100)
	content = models.TextField("내용")
	created_at = models.DateTimeField("등록일", auto_now_add=True)
	# fieldname = models.FieldType("comment", **validate)
```

#### migrate

```
$ python ./manage.py makemigrations
```

If you want to see SQL statements for migrations, you can use `sqlmigrate`

```
$ python ./manage.py sqlmigrate <app_name> <migration_number>
$ python ./manage.py sqlmigrate item 0001
```

```sql
BEGIN;
--
-- Create model Post
--
CREATE TABLE "appname_modelname" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
COMMIT;
```

```
$ python ./manage.py migrate
```
### SQL query

You can use `Manager.raw()` to perform raw queries and return model instances, or you can avoid the model layer entirely and execute custom SQL directly. ([Performing raw SQL queries](https://docs.djangoproject.com/en/2.2/topics/db/sql/))

```python
first_person = Person.objects.raw('SELECT * FROM myapp_person')[0]
```

```python
def ModelManager(models.Manager):
	def with_counts(self):
	     from django.db import connection
	     with connection.cursor() as cursor:
	         cursor.execute("""
	             SELECT p.id, p.question, p.poll_date, COUNT(*)
	             FROM polls_opinionpoll p, polls_response r
	             WHERE p.id = r.poll_id
	             GROUP BY p.id, p.question, p.poll_date
	             ORDER BY p.poll_date DESC""")
	         result_list = []
	         for row in cursor.fetchall():
	             p = self.model(id=row[0], question=row[1], poll_date=row[2])
	             p.num_responses = row[3]
	             result_list.append(p)
	     return result_list
```
To see corresponding SQL query of the Django ORM's queryset, each QuerySet object has a query attribute that you can log or print to stdout for debugging purposes.

```python
qs = Model.objects.filter(name='test')
print(qs.query)
```

If you want to automatically load initial data for an app, just call `manage.py loaddata <fixtures>`

```
$ python ./manage.py loaddata user/fixtures/data.json
$ python ./manage.py loaddata item/fixtures/data.json
$ python ./manage.py loaddata styleshare/fixtures/data.json
$ python ./manage.py loaddata magazie/fixtures/data.json
```
 
You can delete table and data.

```
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc" -delete
$ rm -rf config/db.sqlite3
```

#### dumpdata

```
$ python manage.py dumpdata <app_name>.<model> --indenet 4  > file.json
```
```
$ ./manage.py dumpdata user.User --indent 4 > user/fixtures/data.json
$ ./manage.py dumpdata item.Item --indent 4 > item/fixtures/data.json
$ ./manage.py dumpdata magazine.Magazine --indent 4 > magazine/fixtures/data.json
$ ./manage.py dumpdata styleshare.StyleShare --indent 4 > styleshare/fixtures/data.json
```

## Django Admin

- [http://demo.jet.geex-arts.com/admin/](http://demo.jet.geex-arts.com/admin/)