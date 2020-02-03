#!/usr/bin/Python3 -w

from sqlalchemy import create_engine

db = create_engine('postgresql+psycopg2://@localhost:5432/postgres')

returns = db.connect()
toprint = returns.execute("select * from users")
for r in toprint:
    print(r)