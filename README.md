# paradise-papers
A simple Django web app for searching the Paradise Papers dataset backed by Neo4j

# Requirements

- Django==2.2.6
- django-neomodel==0.0.4
- django-rest-framework==0.1.0
- djangorestframework==3.10.3
- neo4j-driver==1.7.2
- neobolt==1.7.13
- neomodel==3.3.2
- neotime==1.7.4
- pytz==2019.2
- six==1.12.0
- sqlparse==0.3.0


# Quickstart


- Clone this repository

``` bash
# Setup neo4j db and provide credentials in paradise_papers/settings/dev.py file

# Import the data of offshore leaks into the neo4j db

# Go into the repository
cd paradise_papers

# Run the app(after installing requirements)
python manage.py runserver --settings=paradise_papers.settings.dev
```


