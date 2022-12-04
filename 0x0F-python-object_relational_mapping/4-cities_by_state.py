#!/usr/bin/python3
"""Module for getting state from database"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    db = conn.cursor()
    db.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states\
            ON states.id = cities.state_id")

    cities = db.fetchall()
    for city in cities:
        print (city)

    db.close()
    conn.close()
