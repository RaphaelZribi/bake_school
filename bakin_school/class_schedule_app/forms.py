from django import forms 
from class_schedule_app.models import Session
from datetime import datetime


class SessionForm(forms.ModelForm):
	day = forms.DateField(widget = forms.SelectDateWidget(years=range(datetime.now().year + 1, datetime.now().year)))
	#starting_hour = forms.DateField(widget = forms.TimeWidget())
	class Meta():
		model = Session
		fields = ('title', 'description', 'price', 'requirements', 'image', 'chef', 'day', 'starting_hour', 'ending_hour', 'address', 'city')


	
	
	
	
	
	
	
	
	
