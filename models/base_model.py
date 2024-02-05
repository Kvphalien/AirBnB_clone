#!/usr/bin/python3
"""Defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        self.set_attributes(kwargs)

    def set_attributes(self, attribute_dict):
        for attribute, value in attribute_dict.items():
            if attribute in ["created_at", "updated_at"]:
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, attribute, value)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save(self)