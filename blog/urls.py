## formdata.urls.py
## define the URLs for this app

from django.urls import path
from django.conf import settings
from . import views

#define a list of valid URL patterns
urlpatterns = [
    path(r'',views.ShowAllView.as_view(),name="show_all"), 
    #path(r'about', views.about, name="about"),
]
