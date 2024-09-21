## assignment3/urls.py
## description: URL patterns for the assignment3 app

from django.urls import path
from django.conf import settings
from . import views

# all of the URLs that are part of this app
urlpatterns = [
    path(r'', views.home, name="home"),
    path("quote/",views.quote,name="quote"),
    path("show_all/", views.show_all,name="show_all"),
    path("about",views.about,name="about")
]