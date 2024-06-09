from django.contrib import admin
from django.urls import path
from . import views  # Assuming views.py contains the view functions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]
