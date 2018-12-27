from django.db import models
from class_schedule_app.models import Session

class User(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	phone_number = models.TextField()
	email = models.EmailField()
	adress = models.TextField()
	city = models.TextField()
	session = models.ForeignKey(Session, on_delete=models.CASCADE)







