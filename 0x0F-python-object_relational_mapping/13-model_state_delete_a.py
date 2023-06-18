#!/usr/bin/python3
"""
    13-model_state_delete_a.py
    a script that deletes all State objects with
    a name containing the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def delete_state():
    """A function for deleting states object"""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()

    session.close()


if __name__ == '__main__':
    delete_state()
