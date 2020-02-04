# Will be instructions on setting up the entire codebase
The project currently is comprised of:
Database: Dynamodb (to be finally confirmed, mongo is a possible solution too)
Backend: Python Flask-restplus (might migrate to a newer version as restplus isn't constantly updated)
Frontend: Javascript React-app + material-ui

## Postgresql
Setup:
install postgresql onto the computer if not already
Mac: `brew install postgres`
linux ubuntu: `sudo apt-get install postgresql`

install psycopg2 + sqlalchemy
`pip3 install -g pip3`
`pip3 install psycopg2`
