from django.urls import path
from . import views

app_name = 'customers_app'

urlpatterns = [
	path('', views.index, name="index"),
]

