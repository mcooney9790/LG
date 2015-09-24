# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('englishStory', models.TextField(default=b'Story Here')),
                ('chineseStory', models.TextField(default=b'Aqui se queda el cuento')),
                ('spanishStory', models.TextField(default=b'gushi zheli')),
                ('body', models.TextField()),
                ('slug', models.SlugField()),
                ('pub', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Story Entry',
                'verbose_name_plural': 'Story Entries',
            },
        ),
    ]
