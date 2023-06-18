#!/usr/bin/python3
"""
    100-relationship_states_cities.py
    a script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""

from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def add_state():
    """A function for adding new states object"""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

    session.close()


if __name__ == '__main__':
    add_state()
