#!/usr/bin/python3
"""This creates a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
