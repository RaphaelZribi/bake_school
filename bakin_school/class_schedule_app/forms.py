from django import forms 
from class_schedule_app.models import Session


class SessionForm(forms.ModelForm):
	class Meta():
		model = Session
		fields = ('title', 'description', 'price', 'requirements', 'image', 'chef', 'day', 'starting_hour', 'ending_hour', 'address', 'city')

	
	
	
	
	
	
	
	
	
