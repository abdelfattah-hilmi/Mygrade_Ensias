from xmlrpc.client import DateTime
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator 



class Majors(models.Model):

    # A major is a collection of subjects 
    #TODO implement coices for predefind field 

    title = models.CharField(
        max_length = 100,
        unique = True,
        null = False, 
    )
    description = models.TextField(
        max_length = 400,
        blank = True
    )
    


class Subjects(models.Model):
    name = models.CharField(
        max_length = 50
    )


class Grades(models.Model):
    mark = models.SmallIntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(0)
        ]
    )
