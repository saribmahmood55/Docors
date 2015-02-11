# Doctors info. Pakistan
### http://doctorsinfo.pk/
### Installation Instrutions:

1. Installing Data Base, Postgresql 9.3:
```sh
$	sudo apt-get install postgresql-9.3
```

2. Create database with name 'geodjango':
```sh
$	sudo -su postgres
$	createdb geodjango
```
3. Creating postgis extension inside a standard database, we just created i.e 'geodjango', adding a new user and granting privileges to new user:
```sh
$	sudo -u postgres psql geodjango
```
psql commands:
```sh
CREATE EXTENSION postgis;
CREATE USER asadrana WITH PASSWORD 'asad0321';
GRANT ALL PRIVILEGES ON DATABASE "geodjango" to asadrana;
\q
```

4. Install PostGIS Spatial database template for Postgresql 9.3:
```sh
$	sudo apt-get install postgresql postgresql-contrib postgis postgresql-9.3-postgis-2.1
```
5. Create Virtual Environment ('venv' will be good, its already added to .gitignore):
```sh
$	virtualenv venv
```
6. Clone the Repositry:
```sh
$	git clone https://asdi744@bitbucket.org/asdi744/docors.git
```
7. Activate virtual environment:
$	source venv/bin/activate

8. Syncdb
```sh
$	python manage.py syncdb
````
9. Run Migration:
```sh
$	python manage.py migrate
$	python manage.py migrate practice
$	python manage.py migrate practitioner
```
10. Create a Superuser (Highly Recommended):
```sh
$	python manage.py createsuperuser
```
11. Load Fixtures:
```sh
python manage.py loaddata practice practice/fixtures/practice-26-Jan-2015.json
python manage.py loaddata practitioner practitioner/fixtures/practitioner-26-Jan-2015.json
```