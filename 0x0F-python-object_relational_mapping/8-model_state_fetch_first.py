#!/usr/bin/python3
"""
    8-model_state_fetch_first.py
    a script that print the first State object from the database hbtn_0e_6_usa
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

    try:
        state = session.query(State).order_by(State.id).first()
        print("{}: {}".format(state.id, state.name))
    except Exception:
        print()
    finally:
        session.close()


if __name__ == '__main__':
    list_state()
