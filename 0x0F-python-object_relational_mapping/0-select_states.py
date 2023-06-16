#!/usr/bin/python3
# 0-select_states.py
# a script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        host='localhost',
                        port=3306
                            )
    cur = conn.cursor()
    query = "SELECT id,name FROM states ORDER by id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
