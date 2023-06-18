#!/usr/bin/python3
"""
    9-model_state_filter_a.py
    lists all State objects that contain the letter `a`
    from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def list_state():
    """A function for listing states object"""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).\
            filter(State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    list_state()
