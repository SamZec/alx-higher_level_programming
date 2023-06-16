#!/usr/bin/python3
# 1-filter_states.py
# a script that lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa

import MySQLdb
import sys


def List_state():
    db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3])
    conn = db.cursor()
    conn.execute('SELECT * FROM states ORDER BY id')
    for state in conn.fetchall():
        if (state[1][0] == "N"):
            print(state)


if __name__ == '__main__':
    List_state()
