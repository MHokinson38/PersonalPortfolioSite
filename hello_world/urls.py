from django.urls import path
from hello_world import views

#This is very similar to urls.py in the projectPortfolio dir, 
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]