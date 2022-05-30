from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.core.validators import MaxValueValidator,MinValueValidator,MinLengthValidator

class Users(AbstractBaseUser,PermissionsMixin):
    username = None #override username field with none to use email  
    email = models.CharField(
        max_length=255,
        unique=True,
        null=False
        ) #TODO implement email validator
    firstname = models.CharField(
        max_length=255
        ) 
    lastname = models.CharField(
        max_length=255
        )
    password = models.CharField(
        max_length=255,
        blank=False, 
        null=False,
        validators=[MinLengthValidator(8)]
        )
    major = models.ForeignKey(
        'Majors',
        null=True,
        on_delete=models.SET_NULL
        )
    objects = BaseUserManager() #Todo create my custom user manager 
    REQUIRED_FIELDS = ['fistname','lastname','password']
    USERNAME_FIELD = 'email'

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
    def __str__(self):
        return str(self.title)

    


class Subjects(models.Model):
    name = models.CharField(
        max_length = 50
    )
    major = models.ForeignKey(
        'Majors',
        null=True,
        on_delete=models.SET_NULL
        )
    def __str__(self):
        return str(self.name)


class Grades(models.Model):
    mark = models.SmallIntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(0)
        ]
    )
    subject = models.ForeignKey(
        'Subjects',
        null=True,
        on_delete=models.SET_NULL
        )
    user = models.ForeignKey(
        'Users',
        null=True,
        on_delete=models.SET_NULL
        )
