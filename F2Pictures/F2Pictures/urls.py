"""
Definition of urls for F2Pictures.
"""

from django.conf.urls import patterns, include, url
from F2Pictures.Landing import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'F2Pictures.Landing.views.homePage', name='home'),
    url(r'^company/$', views.CompanyList.as_view()),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
