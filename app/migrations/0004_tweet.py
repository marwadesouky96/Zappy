# Generated by Django 2.1.2 on 2018-10-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_delete_tweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=400)),
                ('createdat', models.CharField(max_length=400)),
            ],
        ),
    ]