# Generated by Django 4.0.3 on 2022-03-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_posts_likes_postcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomments',
            name='comment_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
