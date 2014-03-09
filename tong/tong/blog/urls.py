from django.conf.urls import patterns, url
from tong.blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    )