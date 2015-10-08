"""hicks URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Toolbar static pages
    url(  # /
          regex=r'^$',
          view=TemplateView.as_view(template_name='pages/home.html'),
          name='home'),
    url(  # /about/
          regex=r'^about/$',
          view=TemplateView.as_view(template_name='pages/about.html'),
          name='about'),

    # Django Admin
    url(  # /admin/
          regex=r'^admin/',
          view=include(admin.site.urls)),

    # django-allauth
    url(  # /accounts/
          regex=r'^accounts/',
          view=include('allauth.urls')
          ),

    # hicks_language
    url(  # /lang/
          regex=r'^lang/',
          view=include('hicks.hicks_language.urls', namespace='hicks_language'),
          ),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
