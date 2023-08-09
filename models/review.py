#!/usr/bin/python3
"""A module that creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that manages review objects"""

    place_id = ""
    user_id = ""
    text = ""
