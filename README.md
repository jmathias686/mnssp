# Will be instructions on setting up the entire codebase
The project currently is comprised of:

Database: Postgresql + psycopg2/sqlalchemy

    so far: 3 entities within the database, Users, Events, Poll
    do consult `./backend/core/m_schema.sql`

Backend: Python Flask-restplus 

    so far: foundation made, can be expanded upon via namespaces in apis endpoint as well as core for any internal logics

Frontend: Javascript React-app + material-ui
    
    so far: it's a single page application with different components for extension

# Set up
The set up guide is done based on Mac's OSX as was developed on mac book, instructions will be focused on using HomeBrew. 

install HomeBrew if not already, 

`https://brew.sh/`

if developing on Linux, then do use 

`sudo apt-get` instead of `brew`

and ignore downloading HomeBrew

## Backend setup: (python + flask-restplus)
If not already, install python3.7

`brew install python3`

Install Flask micro webapp framework via pip, a python package/module manager

`pip3 install flask`

Install extension for flask

`pip3 install flask-restplus`

The backend should be ready for development.

## Database Setup: (Postgresql + psycopg2/sqlalchemy)
#### install postgresql onto the computer if not already
Mac: `brew install postgres`

linux ubuntu: `sudo apt-get install postgresql`

#### install psycopg2 + sqlalchemy
`pip3 install -g pip3`

`pip3 install psycopg2`

`pip3 install sqlalchemy`

`pip3 install -U flask-cors`
You might need to install a browser extension to allow CORS

#### create postgresql database
stay on root file of mnssp

`pg_ctl init -D ./backend/core/postgres`

#### start postgres and load sample data
`pg_ctl -D ./backend/core/postgres -l logfile start`

`psql ./backend/core/postgres < ./backend/core/m_schema.sql`

`psql ./backend/core/postgres < ./backend/core/dataentry`

The Database will be populated with sample data and is up for development

By default, postgresql will open this on port 5432 to be listened onto, which is what is configured in this project, if any configurations has been made, then do modify accordingly in `mnssp/backend/core/__init__.py`

#### After usage
don't forget to close pg_ctl after usage, otherwise it will keep running!

`pg_ctl -D ./backend/core/postgres stop`



## Front-end Set up
Done in React js using facebook/create-react-app

#### Install NPM used for Javascript

`brew install npm`

#### install package dependency for the frontned apps

`npm install ./frontend/package.json` 

Front end should be ready to go

# Running/Testing development
### Database info
The database is already set up, there will be no need to run it unless you want to input additional fields into the database which can be done by:

`psql ./backend/core/postgres`

which will open a CLI for postgresql for postgresql command manipulation

### Backend
Run the following command to deploy it locally for development testing

`python3 ./backend/app.py`

by default, this will be listening on port 5000 from app.py configuration, this can be adjusted within ./backend/app.py manually based on flask configuration

### Frontend
In Frontend, to test it, it's required to change directory into the Front end project folder via:

`cd frontend`

Run the following command to deploy it locally for development testing

`npm start`

This will start the react app on localhost on port 3000

#### Finally

Feel free extend upon it and deploy it where ever for presentation and hosting

Created by Mufeed Oomatia, Joseph Mathias, Edwin Choi