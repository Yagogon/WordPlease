from django.contrib import admin

# Register your models here.
from posts.models import Post, Category

class PostAdmin(admin.ModelAdmin):

    list_display = ['resume', 'publish_date']

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)