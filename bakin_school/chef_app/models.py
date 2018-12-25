from django.db import models
#from class_schedule_app.models import Session

class Chef(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	description = models.TextField()
	phone_number = models.TextField()
	picture = models.ImageField(upload_to='chefs_pictures', blank=True)
	#session = models.ForeignKey(Session, on_delete=models.CASCADE)