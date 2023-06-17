#!/usr/bin/python3
"""
    1-filter_states.py
    a script that lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb


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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cur.fetchall():
        if (state[1][0] == 'N'):
            print(state)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states()
