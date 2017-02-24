from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^success$', views.success),
    url(r'^travels/add$', views.add),
    url(r'^table$', views.table),
    url(r'^travels/destination/(?P<tid>\d+)', views.destination),
    url(r'^join/(?P<id>\d+)/(?P<tid>\d+)', views.join)
]
