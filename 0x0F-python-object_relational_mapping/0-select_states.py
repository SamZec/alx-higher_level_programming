#!/usr/bin/python3
# 0-select_states.py
# a script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
import sys


def List_state():
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    conn = db.cursor()
    conn.execute('SELECT * FROM states')
    for state in conn.fetchall():
        print(state)


if __name__ == '__main__':
    List_state()
