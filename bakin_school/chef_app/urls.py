from django.urls import path
from . import views

app_name = 'chef_app'

urlpatterns = [
	path('', views.index, name="index"),
]

