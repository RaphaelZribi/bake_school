from django.db import models
from customers_app.models import User 
from class_schedule_app.models import Session


class Enrollment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	place = models.TextField()
	session = models.ForeignKey(Session, on_delete=models.CASCADE, default='')
	date = models.DateField(auto_now=True)