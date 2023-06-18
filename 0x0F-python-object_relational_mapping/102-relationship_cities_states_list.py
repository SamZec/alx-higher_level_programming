#!/usr/bin/python3
"""
    102-relationship_cities_states_list.py
    a script that lists all City objects from the database hbtn_0e_101_usa
"""

from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def list_city():
    """A function listing City objects"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()


if __name__ == '__main__':
    list_city()
