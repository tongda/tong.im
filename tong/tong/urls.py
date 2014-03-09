from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'tong.views.get_home', name='home'),
                       url(r'^home/', include('tong.home.urls', namespace='home')),
                       url(r'^blog/', include('tong.blog.urls', namespace='home')),
                       url(r'^about/', include('tong.about.urls', namespace='home')),
                       # Examples:
                       # url(r'^$', 'tong.views.home', name='home'),
                       # url(r'^tong/', include('tong.foo.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       )
