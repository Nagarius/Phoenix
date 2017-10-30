from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Models listed below based on Dennis' database design. Have excluded some information from
# UserInfo as this information is already present in the default users table.
class UserType(models.Model):
    typeName = models.CharField(max_length=45)
    typeDesc = models.TextField()

    def __str__(self):
        return str(self.typeName)

    def __unicode__(self):
        return smart_unicode(self.typeName)


class City(models.Model):
    cityName = models.CharField(max_length=45, unique=True)
    cityDesc = models.TextField()
    restaurantsLink = models.URLField(default="")
    collegesLink = models.URLField(default="")
    librariesLink = models.URLField(default="")
    librariesLink = models.URLField(default="")
    industriesLink = models.URLField(default="")
    hotelsLink = models.URLField(default="")
    parksLink = models.URLField(default="")
    zoosLink = models.URLField(default="")
    museumsLink = models.URLField(default="")
    mallsLink = models.URLField(default="")
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    latitude = models.DecimalField(max_digits=10, decimal_places=4)


    def __str__(self):
        return str(self.cityName)


class CityInfo(models.Model):
    cityID = models.ForeignKey(City)
    userTypeID = models.ForeignKey(UserType)
    cityInfoName = models.CharField(max_length=45)
    cityInfoDesc = models.TextField()

    def __str__(self):
        return str(self.cityID)


class DataType(models.Model):
    userTypeID = models.ForeignKey(UserType)
    dataName = models.CharField(max_length=45)
    dataDesc = models.TextField()


class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    userTypeID = models.ForeignKey(UserType, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True, default='2016-01-01')
    contactNumber = models.IntegerField(default=2, blank=True)
    address = models.CharField(max_length=50, default='', blank=True)