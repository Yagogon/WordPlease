from posts.models import Post
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ('owner',)

class PostListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ('resume', 'image_url', 'publish_date')
