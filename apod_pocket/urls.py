"""apod_pocket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from request import views
from request.views import MainView, ListView

urlpatterns = [
    url(r'', include(admin.site.urls)),
    url(r'^apods(&limit=(?P<limit>[0-9]+))?(&offset=(?P<offset>[0-9]+))?/$', views.data_detail),
    url(r'^web/$', MainView.as_view()),
    url('web/list/$', ListView.as_view()),
]

