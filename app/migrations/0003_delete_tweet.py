# Generated by Django 2.1.2 on 2018-10-13 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tweet__id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
