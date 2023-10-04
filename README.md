# patriothack2023

##  Django as a fullstack application w/ Bootstrap CDN 
Can possibly use other technologies as well IE : React, FastAPI, Vue, Jinja, Flask, ETC.

Model: Represents a database table and is used to interact with the table.   
View: Contains the logic to handle requests and responses. It interacts with models and templates to display data to the user or accept data from the user.        
Template: An HTML file that displays data. It can incorporate dynamic data, which gets filled in at runtime.      
URL Dispatcher: Directs web requests to the appropriate view based on the request URL.    
Admin Site: A built-in Django feature that provides a web-based interface to manage database records easily.    
Migrations: These are files that Django generates to create or change database tables schematically. The migrate command applies these migrations to the database.    


To run locally, clone the repo and enter this into terminal:


## Setup Instructions

### Clone the Repository
```bash
git clone git@github.com:dangphung4/patriothacks2023.git
cd patriothacks2023
```

Install dependencies with :
```bash
pip install -r requirements.txt
```
Run migrations using :
```bash
cd patriothacks2023

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

### Home URL:
 http://127.0.0.1:8000/

In order to create & run a virtual environment
type these into the terminal:
```bash
python3 -m venv env
.\env\Scripts\activate # for windows users
source ./env/bin/activate # for linux users

pip install -r requirements.txt
pip freeze > requirements.txt

deactivate # to exit virtual enviornment
```
