from django.conf.urls import patterns, url
from tong.about import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^resume$', views.resume, name='resume'),
    url(r'^timeline$', views.timeline, name='timeline'),
    )