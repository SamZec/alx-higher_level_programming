#!/usr/bin/python3
"""
    3-my_safe_filter_states.py
    a script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    that is safe from MySQL injections!
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
    query = """SELECT * FROM states ORDER BY id ASC"""
    cur.execute(query)
    for state in cur.fetchall():
        if (state[1] == argv[4]):
            print(state)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states()
