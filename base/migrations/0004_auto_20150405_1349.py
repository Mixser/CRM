# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150405_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('changed_at', models.DateTimeField(default=django.utils.timezone.now, auto_now=True)),
                ('on_date', models.DateTimeField()),
                ('type', models.IntegerField(choices=[(0, b'Meeting'), (1, b'Task')])),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer', models.OneToOneField(related_name='schedule', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='schedule',
            field=models.ForeignKey(related_name='events', to='base.Schedule'),
            preserve_default=True,
        ),
    ]
