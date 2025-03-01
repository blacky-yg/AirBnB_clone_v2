#!/usr/bin/python3
"""This module defines a user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=True)
    first_name = Column(String(128), nullable=True)
    reviews = relationship("Review", cascade="all, delete", backref="user")
    places = relationship("Place", cascade="all, delete", backref="user")
