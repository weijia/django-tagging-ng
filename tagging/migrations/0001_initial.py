# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, db_index=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': "Tag's synonym",
                'verbose_name_plural': "Tags' synonyms",
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='name', db_index=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='object id', db_index=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('tag_app', models.CharField(help_text='Tag creator', max_length=50, null=True, verbose_name='Tag creator', blank=True)),
                ('content_type', models.ForeignKey(verbose_name='content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(related_name='items', verbose_name='tag', to='tagging.Tag')),
            ],
            options={
                'verbose_name': 'tagged item',
                'verbose_name_plural': 'tagged items',
            },
        ),
        migrations.AddField(
            model_name='synonym',
            name='tag',
            field=models.ForeignKey(related_name='synonyms', to='tagging.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='taggeditem',
            unique_together=set([('tag', 'content_type', 'object_id')]),
        ),
    ]
