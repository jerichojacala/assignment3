#blog/view.py
#dfine the views for the blog app

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import * #import the models

#class-based view
class ShowAllView(ListView):
    '''the view to show all Articles'''
    model = Article #the model to display
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' #this is the context variables to use in the template
    
