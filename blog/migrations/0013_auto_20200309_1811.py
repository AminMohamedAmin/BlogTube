# Generated by Django 2.2.3 on 2020-03-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200309_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-puplish',), 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
