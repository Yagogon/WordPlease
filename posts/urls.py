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
from django.conf.urls import  url
from posts.views import HomeView, PostListViewByUser, PostDetailView, PostListView, VanillaCreateView


urlpatterns = [

    url(r'^$', HomeView.as_view(), name="posts_home"),
    url(r'posts/new$', VanillaCreateView.as_view(), name="create_post"),
    url(r'posts/$', PostListView.as_view(), name="all_posts"),
    url(r'posts/([0-9a-zA-Z]+)$', PostListViewByUser.as_view(), name='list_post'),
    url(r'^posts/(?P<loginname>[0-9a-zA-Z]+)/(?P<post_id>[0-9]+)$',PostDetailView.as_view(), name='posts_detail')

]
