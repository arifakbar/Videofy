# Generated by Django 3.1.1 on 2020-10-07 06:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0018_auto_20201007_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='history',
        ),
        migrations.AddField(
            model_name='uservideo',
            name='history',
            field=models.ManyToManyField(related_name='user_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
