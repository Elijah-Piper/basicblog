# Generated by Django 3.1.2 on 2020-10-06 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201006_0102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_post', 'Can author blog posts'),)},
        ),
    ]
