#!/usr/bin/Python3 -w

from sqlalchemy import create_engine

db = create_engine('postgresql+psycopg2://@localhost:5432/postgres')

dbquery = db.connect()
# for r in toprint:
#     print(r)

#returns tuples of entries, loop to show
def queryDB(query):
    qobject = dbquery.execute(query)
    arrays = []
    for r in qobject:
        arrays.append(r)
    return arrays

def commitDB(query):
    dbquery.execute(query)
    dbquery.commit()
    return


