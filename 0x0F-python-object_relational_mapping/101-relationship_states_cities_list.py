#!/usr/bin/python3
"""
    101-relationship_states_cities_list.py
    a script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""

from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def list_state_city():
    """A function listing State and coresponding City objects"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()


if __name__ == '__main__':
    list_state_city()
