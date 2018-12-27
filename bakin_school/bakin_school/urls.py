"""bakin_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from class_schedule_app import views
from customers_app import views
from chef_app import views
from enrollment_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('class_schedule_app/', include ('class_schedule_app.urls')),
    path('customers_app/', include('customers_app.urls')),
    path('chef_app/', include('chef_app.urls')),
    path('enrollment_app/', include('enrollment_app.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
