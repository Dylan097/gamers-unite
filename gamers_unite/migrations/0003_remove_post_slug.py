# Generated by Django 3.2.16 on 2022-11-07 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers_unite', '0002_remove_post_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
