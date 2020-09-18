from django.shortcuts import render

#Import the models from project 
from projects.models import Project 

def project_index(request):
    projects = Project.objects.all() # Performs query do get all of the objects in the projects table (Project was defined in models.py)

    context = {
        'projects': projects
    } # Here we are defining a dictionary that we can send to our template when we render the page 
    # Every view function needs to have a context dictionary

    return render(request, 'project_index.html', context) #project_index.html is going to be a template that we have in projects. 

def project_detail(request, pk):
    project = Project.objects.get(pk = pk)

    context = {
        'project': project 
    }

    return render(request, 'project_detail.html', context)