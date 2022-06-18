from email import message
from functools import reduce
from django.db import models
from datetime import datetime


# Create your models here.


#creating models for user

class userform(models.Model):
	dob = models.IntegerField()
	gender = models.IntegerField(max_length=100)
	hight = models.IntegerField(max_length=100)
	wbr = models.IntegerField(max_length=100)
	war = models.IntegerField(max_length=100)
	acti = models.IntegerField(max_length=100)
	yav = models.CharField(max_length=100)


	feeling = models.CharField(max_length=100)
	hadache = models.CharField(max_length=100)
	lathrgy = models.CharField(max_length=100)
	reduce = models.CharField(max_length=100)
	wtl = models.CharField(max_length=100)
	dic = models.CharField(max_length=100)
	loi = models.CharField(max_length=100)
	fsleepy = models.CharField(max_length=100)
	bodypain = models.CharField(max_length=100)
	disease = models.CharField(max_length=100)
	usernamenew=models.CharField(max_length=100)
	'''date=models.DateTimeField(("date"), auto_now=False, auto_now_add=False)'''
	date=models.DateTimeField(default=datetime.now())

# creating model for feedback

class feedback(models.Model):
	message = models.CharField(max_length=122)

# creating models for login_register

class login_register(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	

class contact(models.Model):
    name = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    msg= models.TextField()
   



