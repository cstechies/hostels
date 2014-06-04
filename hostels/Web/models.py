from django.db import models
from djangotoolbox.fields import DictField


class Hostels(models.Model):
    name = models.TextField()
    contactNo = models.IntegerField()
    rating = models.IntegerField()
    address = DictField()