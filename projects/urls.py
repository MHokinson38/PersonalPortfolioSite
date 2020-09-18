from django.urls import path
from . import views 

# Declare the template paths that we are going to create for Project app. 
# The notation in the second path allows us to dynamically generate a url prefix based on the 
# project number <int:pk> notation. This is telling Django that the value passed is an int, and the variable name is 
# pk. Basically, when you look at the url, rather than seeing higherStuff/projects/something here, you will see higherStuff/projects/pk  

# **NOTE** urlpatterns needs to be this name 
urlpatterns = [
    path("", views.project_index, name="project_index"), # Our URL will look like higherStuff/projects
    path("<int:pk>/", views.project_detail, name="project_detail"), # .../projects/3 if pk=3
]