#!/usr/bin/python3
# 3-my_safe_filter_states.py
# a script that takes in arguments and displays all values in the states table
# of hbtn_0e_0_usa where name matches the argument
# that is safe from MySQL injections!

import MySQLdb
import sys


def List_state():
    """A function that list states base on arg"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    conn = db.cursor()
    conn.execute('SELECT * FROM states ORDER BY id')
    for state in conn.fetchall():
        if (state[1] == "{}".format(sys.argv[4])):
            print(state)


if __name__ == '__main__':
    List_state()
