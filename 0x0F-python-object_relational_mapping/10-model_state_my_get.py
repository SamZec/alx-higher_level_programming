#!/usr/bin/python3
"""
    10-model_state_my_get.py
    prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
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

    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if (state is None):
        print('Not found')
    else:
        print("{}".format(state.id))
    session.close()


if __name__ == '__main__':
    list_state()
