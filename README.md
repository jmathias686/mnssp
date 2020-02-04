# Will be instructions on setting up the entire codebase
The project currently is comprised of:
Database: Dynamodb (to be finally confirmed, mongo is a possible solution too)
Backend: Python Flask-restplus (might migrate to a newer version as restplus isn't constantly updated)
Frontend: Javascript React-app + material-ui

## Postgresql
### Setup:
#### install postgresql onto the computer if not already
Mac: `brew install postgres`
linux ubuntu: `sudo apt-get install postgresql`

#### install psycopg2 + sqlalchemy
`pip3 install -g pip3`
`pip3 install psycopg2`
`pip3 install sqlalchemy`

#### create postgresql database
stay on root file of mnssp
`pg_ctl init -D ./backend/core/postgres`

#### start postgres and load sample data
`pg_ctl -D ./backend/core/postgres -h logfile start`
`psql ./backend/core/postgres < ./backend/core/m_schema.sql`
`psql ./backend/core/postgres < ./backend/core/dataentry`

#### After usage
don't forget to close pg_ctl
`pg_ctl -D ./backend/core/postgres stop`