from django.db import models
from chef_app.models import Chef 
from enrollment_app.models import Enrollment

class Session(models.Model):
	title         = models.TextField()
	description   = models.TextField()
	price         = models.IntegerField()
	requirements  = models.TextField(blank=True)
	image         = models.ImageField(upload_to='images/sessions', blank=True)
	chef          = models.ForeignKey(Chef, on_delete=models.CASCADE)
	day           = models.DateField(default='01/01/2001')
	starting_hour = models.TimeField(default='16h30')
	ending_hour   = models.TimeField(default='19h30')
	address       = models.TextField(default='13 Karlibar Street')
	city          = models.TextField(default='Tel-Aviv')
	enrollment    = models.ForeignKey(Enrollment, on_delete=models.CASCADE, blank=True)
	


