from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process$', views.process, name="index"),
    url(r'^formresults$', views.formresults, name="results"),
    url(r'^reset$', views.reset, name="reset")
]