from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserType(models.Model):
    typeName = models.CharField(max_length=45)
    typeDesc = models.TextField()


class City(models.Model):
    cityName = models.CharField(max_length=45)
    cityDesc = models.TextField()


class CityInfo(models.Model):
    cityID = models.ForeignKey(City)
    userTypeID = models.ForeignKey(UserType)
    cityInfoName = models.CharField(max_length=45)
    cityInfoDesc = models.TextField()


class DataType(models.Model):
    userTypeID = models.ForeignKey(UserType)
    dataName = models.CharField(max_length=45)
    dataDesc = models.TextField()


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userTypeID = models.ForeignKey(UserType)
    dob = models.DateField()
    contactNumber = models.IntegerField()
    address = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userinfo.save()

    def __str__(self):
        return str(self.address)