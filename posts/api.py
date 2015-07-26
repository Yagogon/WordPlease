from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.timezone import now
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import BlogSerializer, PostListSerializer, PostDetailSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet, ModelViewSet

class PostQueryset(object):

    def get_post_queryset(self):

        if not self.request.user.is_authenticated():
            posts = Post.objects.filter(publish_date__lte=now).order_by('-publish_date')

        elif self.request.user.is_superuser:
            posts = Post.objects.all().order_by('-publish_date')

        else:
            posts = Post.objects.filter(Q(owner=self.request.user) | Q(publish_date__lte=now)).order_by('-publish_date')

        return posts

class BlogViewSet(ListModelMixin, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = BlogSerializer
    search_fields = ('username',)
    ordering_fields = ('username',)
    filter_backends = (SearchFilter, OrderingFilter)



class PostViewSet(ModelViewSet, PostQueryset):

    serializer_class = PostListSerializer
    permission_classes = (PostPermission,)
    search_fields = ('resume','body')
    ordering_fields = ('publish_date',)
    filter_backends = (SearchFilter, OrderingFilter)

    def get_queryset(self):
        return self.get_post_queryset()

    def get_serializer_class(self):

        if (self.action == 'list'):
            return PostListSerializer
        else:
            return PostDetailSerializer

    def perform_create(self, serializer):
        """
        Asigna automaticamente la autoria de la nueva foto al usuario autenticado
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)




