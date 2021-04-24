from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index")
]

app_name = 'advice'