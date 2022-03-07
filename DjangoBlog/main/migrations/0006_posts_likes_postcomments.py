# Generated by Django 4.0.3 on 2022-03-06 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.posts')),
            ],
            options={
                'verbose_name': 'Post comment',
                'verbose_name_plural': 'Post comments',
            },
        ),
    ]
