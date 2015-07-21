# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resume', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('image_url', models.URLField(null=True)),
                ('publish_date', models.DateTimeField()),
                ('categories', models.CharField(max_length=3, null=True, choices=[(b'gam', b'games'), (b'food', b'food'), (b'TEC', b'technology')])),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
