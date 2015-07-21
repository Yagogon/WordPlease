from django.db import models
from django.contrib.auth.models import User


# Create your models here.

GAMES = "gam"
FOOD = "foo"
TECHNOLOGY ="tec"

CATEGORIES = (
    (GAMES, 'games'),
    (FOOD, 'food'),
    (TECHNOLOGY, 'technology')
)

class Category(models.Model):

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Post(models.Model):

    owner = models.ForeignKey(User)
    resume = models.CharField(max_length=300)
    body = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    publish_date = models.DateField()
    categories = models.ForeignKey(Category, null=True, blank=True)

    def __unicode__(self):
        return self.resume

