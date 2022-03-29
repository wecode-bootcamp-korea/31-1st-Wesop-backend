from django.db import models

from cores.timestamp import TimeStamp

# Create your models here.
class User(TimeStamp):
    first_name = models.CharField(max_length=40, null=False)
    last_name  = models.CharField(max_length=40, null=False)
    email      = models.EmailField(unique=True, max_length=100)
    password   = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'