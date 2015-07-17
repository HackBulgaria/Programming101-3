# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_projection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(to='website.Movie'),
        ),
    ]
