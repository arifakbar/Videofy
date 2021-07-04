# Generated by Django 3.1.1 on 2020-10-31 05:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0019_auto_20201007_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='video_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='history',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_history', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='video_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='watchLater',
            field=models.ManyToManyField(blank=True, null=True, related_name='watch_later', to=settings.AUTH_USER_MODEL),
        ),
    ]
