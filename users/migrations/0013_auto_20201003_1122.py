# Generated by Django 3.1.1 on 2020-10-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_userplaylist_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservideo',
            name='trending',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uservideo',
            name='trendingTop5',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
