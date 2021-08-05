from django.urls import path, include, re_path
from django.conf.urls import url

# App to App Modules
from .import views

# external modules

urlpatterns = [
    path('', views.index, name='INDEX',kwargs={}),
    path('delete/', views.DeleteFile, name='DELETE'),
    path('sms-result/', views.send_sms_result, name='SMS'),
    # path('mail-result/', views.send_mail_result, name='MAIL'),

    # path('test/', views.test, name='test'),
    # re_path(r'^$', views.index, name='index'),
]
