from django.urls import path
from . import views

app_name = 'enrollment_app'

urlpatterns = [
	path('', views.index, name="index"),
]

