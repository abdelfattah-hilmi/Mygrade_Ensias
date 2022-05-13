from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator 

class Grades(models.Model):
    Mark = models.SmallIntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(0)
        ]
    )
