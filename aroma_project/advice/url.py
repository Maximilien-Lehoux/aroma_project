from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^advice_he/$', views.advice_he, name="advice_he")
]

app_name = 'advice'