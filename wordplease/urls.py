"""wordplease URL Configuration

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
from users import api_urls as users_api_urls, urls as users_urls
from posts import api_urls as posts_api_urls, urls as posts_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'api/', include(users_api_urls)),
    url(r'api/', include(posts_api_urls)),

    url(r'', include(posts_urls)),

    url(r'', include(users_urls)),



]
