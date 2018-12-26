from django import forms 
from chef_app.models import Chef

class ChefForm(forms.ModelForm):
	class Meta():
		model = Chef
		fields = ('first_name', 'last_name', 'description', 'phone_number', 'picture')


