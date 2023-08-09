#!/usr/bin/python3
"""A module that creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class that manages city objects"""

    state_id = ""
    name = ""
