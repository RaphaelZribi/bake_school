from django.db import models

class User(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	phone_number = models.TextField()
	email = models.EmailField()
	adress = models.TextField()
	city = models.TextField()







