from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from chef_app.forms import ChefForm

def chefForm(request):
	if request.method =='POST':
		chef_form = ChefForm(request.POST, request.FILES)
		if chef_form.is_valid():
			new_chef = chef_form.save()
			if 'picture' in request.FILES:
				chef_form.picture = request.FILES['picture']
			return HttpResponse('thank You!!')
	else: 
		chef_form = ChefForm()
	return render(request, 'chefForm.html', {'chef_form':chef_form})


