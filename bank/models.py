from django.db import models
from django.db.models.fields import IntegerField


class user(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    amount_add = models.IntegerField()

# Create your models here.
