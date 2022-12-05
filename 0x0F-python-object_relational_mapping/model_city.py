#!/usr/bin/python3
"""Module hat contains the class definition of a State and an
    instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """ORM class for cities"""
    __tablename__ = 'cities'
    id  = Column(Integer, primary_key=True, nullable=False, unique=True,
            autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
