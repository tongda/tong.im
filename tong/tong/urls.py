from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'tong.views.get_home', name='home'),
    url(r'^home/', include('tong.home.urls', namespace='home')),
    url(r'^blog/', include('tong.blog.urls', namespace='blog')),
    url(r'^about/', include('tong.about.urls', namespace='about')),
    )
