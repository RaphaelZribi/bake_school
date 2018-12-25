from django.db import models
from chef_app.models import Chef 
from enrollment_app.models import Enrollment



class Date(models.Model):
	day = models.DateField()
	starting_hour = models.TimeField()
	ending_hour = models.TimeField()


class Location(models.Model):
	adress = models.TextField()
	city = models.TextField()


class Session(models.Model):
	title = models.TextField()
	description = models.TextField()
	price = models.IntegerField()
	requirements = models.TextField(blank=True)
	image = models.ImageField(blank=True)
	date = models.ForeignKey(Date, on_delete=models.CASCADE)
	chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
	


