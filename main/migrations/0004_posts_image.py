# Generated by Django 4.0.3 on 2022-03-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_users_administrator_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]