from django.db import models

# Create your models here.
# This is where we create models using the ORM (Object relational mapper), which Django has built in to work with SQL databases

# General Notes 
# TextField is similar to CharField in that they store strings, but CharField is for shorter length strings and it requires a max limit 
# FilePathField also holds a string, but that string must be a valid file path 
#
# By Default, Django creates databases using ORM to make SQLite, but you can use other SQL databases, such as PostgreSQL or MrSQL 
#
#
#

# =========================
# Model for Project 
# =========================
class Project(models.Model):
    # Declare our fields and assign limits to those fields 
    title = models.CharField(max_length = 100) # The name of the project 

    description = models.TextField() # Holds the Description of the project 

    technology = models.CharField(max_length = 20) # Another string with max length 

    image = models.FilePathField( path = "/img" ) # Image field that stores that path to the image we want to display 
