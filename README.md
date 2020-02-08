# Instructions for setup of codebase
The project currently is comprised of:

**Database:** *Postgresql + psycopg2/sqlalchemy*
    
    3 entities within the database - Users, Events, Poll
    do consult `./backend/core/m_schema.sql`

**Backend:** *Python Flask-restplus*
    
    Foundation made, can be expanded upon via namespaces in apis endpoint as well as core for any internal logics

**Frontend:** *Javascript React-app + material-ui*
    
    Multi page application with different components for extension

# Set up
The set up guide is done based on Mac's OSX as was developed on mac book, instructions will be focused on using HomeBrew. 

Install HomeBrew if not already:

**Homebrew Page:** [brew.sh](https://brew.sh/)

If developing on Linux, then use 

`sudo apt-get` instead of `brew`

*Alternatively - you may install homebrew for linux or a WSL system and follow the below instructions*

## Backend + Database Setup (Simple setup)
*If you wish to do a full setup and avoid installing redundant libraries, skip to Backend Setup*

If not already, install python3.x

`brew install python3`

If not already, install postgresql onto computer

`brew install postgres`

Install pip3 libraries: *Make sure you are in the base directory /mnssp*

`pip3 install -r requirements.txt`

## Manual Setup for Backend + Database
### Backend setup: (python + flask-restplus)
If not already, install python3.x

`brew install python3`

Install Flask micro webapp framework via pip, a python package/module manager

`pip3 install flask`

Install extension for flask

`pip3 install flask-restplus`

Install CORS extension for flask

`pip3 install -U flask-cors`
You might need to install a browser extension to allow CORS

The backend should be ready for development.

### Database Setup: (Postgresql + psycopg2/sqlalchemy)
#### install postgresql onto the computer if not already
Mac: `brew install postgres`

linux ubuntu: `sudo apt-get install postgresql`

#### install psycopg2 + sqlalchemy
`pip3 install -g pip3`

`pip3 install psycopg2`

*Note: If you have issues installing psycopg2, you might need to run:*
`pip3 install psycopg2-binary`

`pip3 install sqlalchemy`

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
Created in React js using facebook/create-react-app

#### Install NPM used for Javascript

`brew install npm`

#### install package dependency for the frontned apps

`npm install ./react-mnssp-ui/package.json` 

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

`cd react-mnssp-ui/src`

Run the following command to deploy it locally for development testing

`npm start`

This will start the react app on localhost on port 3000

#### Finally

Feel free extend upon it and deploy it where ever for presentation and hosting

Created by Mufeed Oomatia, Joseph Mathias, Edwin Choi