from django.db import models
from djangotoolbox.fields import DictField, ListField

class Hostels(models.Model):
    name = models.TextField()
    contactNo = models.IntegerField(null=True)
    avgRating = models.IntegerField()
    rating = DictField(null=True)
    gmapsReference = models.TextField()
    ownerName = models.TextField(default="Techie")
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    rentMin = models.IntegerField(null=True)
    rentMax = models.IntegerField(null=True)
    rentDesc = models.TextField(null=True)
    gender = models.TextField(null=True)
    miscellaneous = DictField(null=True)
    regBy = models.TextField(default="admin")