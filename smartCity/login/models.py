from django.db import models

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
    userTypeID = models.ForeignKey(UserType)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=30)
    fName = models.CharField(max_length=45)
    lName = models.CharField(max_length=45)
    dob = models.DateField()
    email = models.EmailField(max_length=45)
    contactNumber = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.address)