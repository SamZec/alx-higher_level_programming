#!/usr/bin/python3
"""
    2-my_filter_states.py
    a script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
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
    query = """SELECT * FROM states WHERE BINARY name = '{:s}'
            ORDER BY id ASC""".format(argv[4])
    cur.execute(query)
    for state in cur.fetchall():
        print(state)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states()
