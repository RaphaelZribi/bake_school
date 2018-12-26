from django.urls import path
from . import views

app_name = 'class_schedule_app'

urlpatterns = [
	path('all_sessions/', views.all_sessions, name='all_sessions'),
	path('session_description/<int:session_id>/', views.session_description, name='session_description'),
	path('new_session/', views.new_session, name="new_session"),
]

