#!/usr/bin/python3
"""
    relationship_state.py
    a python file that contains the class definition of a State
    related to City
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """A class that inherit from Base = declarative_base()"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
