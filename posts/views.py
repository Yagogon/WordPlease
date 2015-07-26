from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import View
from vanilla import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from posts.forms import PostForm
from posts.models import Post

class VanillaCreateView(CreateView):

    model = Post
    success_url = reverse_lazy('create_post')

    def get_form(self, data=None, files=None, **kwargs):

        return PostForm(data, files, **kwargs)

    def form_valid(self, form):

        post = form.save(commit=False)
        post.owner = self.request.user
        post.save()

        context = {

            'form': PostForm()
        }

        return render(self.request, 'posts/post_form.html', context)


class HomeView(View):

    def get(self, request):
        """
        Devuelve el home de la pagina

        """
        posts = Post.objects.filter(publish_date__lte=now).order_by('-publish_date')

        context = {

            'posts': posts
        }
        return render(request, 'posts/home.html', context)

class CreateView(View):

    def get(self, request):

        form = PostForm()

        context = {

            'form': form
        }

        return render(request, 'posts/new_post.html', context)

    def post(self, request):

        post_with_owner = Post()
        post_with_owner.owner = request.user
        form = PostForm(request.POST, instance=post_with_owner)

        if form.is_valid():
            new_post = form.save()
            form = PostForm()


        context = {

                'form': form,
        }

        return render(request, 'posts/new_post.html',context)


class PostListViewByUser(View):

    def get(self, request, username):

        if request.user.username == username:

            context = {

            'posts': Post.objects.filter(owner__username=username).order_by('-publish_date')

            }

        else:

            context = {

            'posts': Post.objects.filter(owner__username=username, publish_date__lte = now).order_by('-publish_date')

            }


        return render(request, 'posts/posts_list.html', context)

class BlogListView(View):

    def get(self, request):

        users = User.objects.all()
        blogs = {}

        for user in users:

            if user == request.user:
                user_blog = Post.objects.filter(owner=user).order_by('publish_date')
            else:
                user_blog = Post.objects.filter(owner=user, publish_date__lte = now).order_by('publish_date')


            if len(user_blog) > 0:
                blogs[user] = user_blog

        context = {

            'blogs': blogs,

        }

        return render(request, 'posts/blogs_list.html', context)


class PostDetailView(View):

    def get(self, request, post_id, loginname):

        possible_posts = Post.objects.filter(pk=post_id, owner__username=loginname).select_related('owner')
        post = possible_posts[0] if len(possible_posts) >=1 else None

        if post is not None:

            context = {

                'post': post

            }

            return render(request, 'posts/detail.html', context)
        else:
            return HttpResponseNotFound('No existe la foto')