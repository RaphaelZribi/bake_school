from django.shortcuts import render
from django.http import HttpResponse
from class_schedule_app.models import Session


def all_sessions(request):
	sessions = Session.objects.all()
	return render(request, 'all_sessions.html', {'sessions': sessions})

def session_description(request, session_id):
	session = Session.objects.get(id=session_id)
	return render (request, 'session_description.html', {'session':session})

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


