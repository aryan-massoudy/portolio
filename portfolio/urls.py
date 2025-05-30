# portfolio/urls.py
from django.urls import path
from . import views

app_name = 'portfolio' # This is key!

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
]