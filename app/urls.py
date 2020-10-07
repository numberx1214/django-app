from django.conf.urls import url
from django.urls import path

from . import views

app_name='app1'
urlpatterns = [
    url(r'^$', views.base, name='home'),
    url(r'^news$', views.news, name='news'),
    url(r'^blog$', views.blog, name='blog'),
]
