from django.conf.urls import patterns, url
from tong.home import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'))
