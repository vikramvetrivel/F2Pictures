"""
Definition of urls for F2Pictures.
"""

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'F2Pictures.Landing.views.homePage', name='home'),
    # url(r'^F2Pictures/', include('F2Pictures.F2Pictures.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),



    #This should be the last URL.
    url(r'^.*$', 'F2Pictures.Landing.views.homePage'),   
)
