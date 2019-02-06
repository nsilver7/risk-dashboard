from django.conf.urls import patterns, url

from riskDashboard2 import views

urlpatterns = patterns('',
    #url(r'getdata', views.vulnData, name='getdata'),
    url(r'appmanagement', views.appmanagement, name='appmanagement'),
    url(r'^.*', views.index, name='index'),
)
