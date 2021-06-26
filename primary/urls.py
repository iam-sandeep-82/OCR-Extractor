from django.urls import path, include, re_path
from django.conf.urls import url

# App to App Modules
from .import views


urlpatterns = [
    path('', views.index, name='index',kwargs={}),
    # re_path(r'^$', views.index, name='index'),
]
