# Generated by Django 2.2.3 on 2020-03-08 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='user',
            field=models.CharField(max_length=150),
        ),
    ]
