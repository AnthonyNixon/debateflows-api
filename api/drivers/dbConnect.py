#!flask/bin/python
import MySQLdb
import os

def connect():
    DBHOST = os.environ['DBHOST']
    DBUSER = os.environ['DBUSER']
    DBPASS = os.environ['DBPASS']

    # Set up DB connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, "debateflows")
    return db