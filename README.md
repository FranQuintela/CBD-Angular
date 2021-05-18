# CBD-Angular 1
The first step is to create a virtual environment that will will englobe all the requirements. So let’s start by installing virtualenv and activate the virtual environment:
$ pip install virtualenv
$ virtualenv env
$ env\Scripts\activate
Then we install django and django_neomodel:
$ pip install Django
$ pip install django_neomodel
Finally, we install Neo4j. For that i recommend you to use the official documentation of Neo4j. You can find it here.
We are ready now to start creating our django API.

in django back_end -> settings.py replace username and password with the data we used on the neo4J desktop 
NEOMODEL_NEO4J_BOLT_URL = os.environ.get('NEO4J_BOLT_URL','bolt://username:password@localhost:7687')

pip install django-cors-headers

create models on models.py
create index and constraints with: python manage.py install_labels

run scripts to load csv and MATCH relationships


Para hacer un reset de la bd: CREATE OR REPLACE DATABASE neo4j
