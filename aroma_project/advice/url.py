from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^advice_he/$', views.advice_he, name="advice_he"),
    url(r'^admin_database/$', views.admin_database, name="admin_database"),
]

app_name = 'advice'