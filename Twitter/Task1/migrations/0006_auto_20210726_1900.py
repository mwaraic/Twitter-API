# Generated by Django 2.2.12 on 2021-07-26 19:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task1', '0005_friends'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together={('handle1', 'handle2')},
        ),
    ]
