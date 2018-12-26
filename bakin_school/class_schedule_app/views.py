from django.shortcuts import render
from django.http import HttpResponse
from class_schedule_app.forms import SessionForm



def new_session(request):
	if request.method =='POST':	
		form = SessionForm(request.POST, request.FILES)
		if form.is_valid():
			session = form.save()
			if 'image' in request.FILES:
				form.image = request.FILES['image']
			
			return HttpResponse('New Class Created!')
	else: 
		form = SessionForm()
	return render(request, 'new_sessions.html', {'form': form})


