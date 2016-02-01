"""
Definition of urls for F2Pictures.
"""

from django.conf.urls import patterns, include, url
from F2Pictures.Landing import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
admin.autodiscover()

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'portfolio', views.PortfolioViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'project', views.ProjectViewSet)

urlpatterns = patterns('',
    url(r'^$', 'F2Pictures.Landing.views.homePage', name='home'),
    url(r'^packery/', 'F2Pictures.Landing.views.packery', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),  
)
