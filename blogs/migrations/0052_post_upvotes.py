# Generated by Django 4.0.4 on 2022-06-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0051_post_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
