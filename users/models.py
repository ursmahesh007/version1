'''
A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table.

The basics:
Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API.

https://docs.djangoproject.com/en/3.0/topics/db/models/
'''
# users/models.py
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.auth.models import AbstractUser
# from django.db import models
from djongo import models
