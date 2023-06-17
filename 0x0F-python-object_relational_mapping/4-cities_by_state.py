#!/usr/bin/python3
"""
    4-cities_by_state.py
    a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def list_states():
    """A function that list states"""
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    query = """
                SELECT city.id, city.name, state.name FROM cities as city
                INNER JOIN states as state ON city.state_id = state.id
                ORDER BY city.id ASC
            """
    cur.execute(query)
    for city in cur.fetchall():
        print(city)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states()
