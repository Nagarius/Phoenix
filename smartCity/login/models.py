from django.db import models

# Create your models here.
class userInfo(models.Model):
    userID = models.IntegerField(max_length=10)
    userTypeID = models.ForeignKey(userType, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.CharField(50)
    contactNumber = models.IntegerField(max_length=50)
    address = models.CharField(50)

class userType(models.Model):
    typeName = models.CharField(max_length=50)
    typeDesc = models.TextField()
    userTypeID = models.CharField(max_length=1, choices=USER_TYPE)

    USER_TYPE = (
        ('T', 'Tourist'),
        ('B', 'Business'),
        ('S', 'Student'),
        ('A', 'Administrator'),
    )
