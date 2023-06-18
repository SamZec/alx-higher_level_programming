#!/usr/bin/python3
"""
    12-model_state_update_id_2.py
    a script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def update_state():
    """A function for updating states object"""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()

    session.close()


if __name__ == '__main__':
    update_state()
