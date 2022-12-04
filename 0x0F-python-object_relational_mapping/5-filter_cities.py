#!/usr/bin/python3
"""Module for getting state from database"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    db = conn.cursor()
    db.execute("SELECT cities.name FROM cities JOIN states\
            ON states.id = cities.state_id\
            WHERE states.name = %(states.name)s", {'states.name': argv[4]})

    lists = []
    cities = db.fetchall()
    for city in cities:
        lists += city
    print(", ".join(lists))

    db.close()
    conn.close()
