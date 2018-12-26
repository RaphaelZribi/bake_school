from django.urls import path
from . import views

app_name = 'class_schedule_app'

urlpatterns = [
	path('new_session/', views.new_session, name="new_session"),
]

