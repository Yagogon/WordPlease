from django.contrib.auth.models import User
from django.utils.timezone import now
from posts.models import Post
from rest_framework import serializers


class BlogSerializer(serializers.Serializer):

    blog_name = serializers.SerializerMethodField()
    blog_url = serializers.SerializerMethodField()
    number_of_post = serializers.SerializerMethodField()

    class Meta:

        model = User

    def get_blog_name(self, user):
        return 'Blog de ' + user.username

    def get_blog_url(self, user):
        return 'http://127.0.0.1:8000/posts/' + user.username

    def get_number_of_post(self, user):
        return len(Post.objects.filter(owner=user,publish_date__lte=now))



class PostListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ('resume', 'image_url', 'publish_date')

class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        read_only_fields = ('owner',)
        exclude = []
