#!/usr/bin/Python3 -w

from sqlalchemy import create_engine

db = create_engine('postgresql+psycopg2://@localhost:5432/postgres')

# for r in toprint:
#     print(r)

#returns tuples of entries, loop to show
def queryDB(query):
    dbquery = db.connect()
    qobject = dbquery.execute(query)
    arrays = []
    for r in qobject:
        arrays.append(r)
    dbquery.close()
    return arrays

def commitDB(query):
    dbquery = db.connect()
    dbquery.execute(query)
    dbquery.close()
    return


