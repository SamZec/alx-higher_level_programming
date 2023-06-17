#!/usr/bin/python3
"""
    model_state.py
    a python file that contains the class definition of a State
    and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class that inherit from Base = declarative_base()"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
