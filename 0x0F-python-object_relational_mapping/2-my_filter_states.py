#!/usr/bin/python3
"""Module for getting state from database"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    db = conn.cursor()
    db.execute("""SELECT * FROM states WHERE name like '%s'""" %(argv[4]))

    states = db.fetchall()
    for state in states:
        print (state)

    db.close()
    conn.close()
