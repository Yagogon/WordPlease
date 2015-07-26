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
from posts.api import PostViewSet, BlogViewSet
from rest_framework.routers import DefaultRouter


# APIRouter
router = DefaultRouter()
router.register(r'posts', PostViewSet, base_name='post')
router.register(r'blogs', BlogViewSet, base_name='blog')


urlpatterns = [

    url(r'1.0/', include(router.urls))

]

