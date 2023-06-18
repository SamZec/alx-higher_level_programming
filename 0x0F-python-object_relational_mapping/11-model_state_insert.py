#!/usr/bin/python3
"""
    11-model_state_insert.py
    a script that adds State object “Louisiana” to the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def add_state():
    """A function for adding new states object"""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    nstate = State(name='Louisiana')
    session.add(nstate)
    session.commit()

    state = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(state.id))
    session.close()


if __name__ == '__main__':
    add_state()
