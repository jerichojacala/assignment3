#mini_fb/views.py
#define the views for the blog app

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import * #import the models

#class-based view
class ShowAllProfilesView(ListView):
    '''the view to show all Articles'''
    model = Profile #the model to display
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' #this is the context variables to use in the template
    
