# Generated by Django 3.1.2 on 2020-10-06 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201006_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name', 'account_username']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-posted']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['posted'], 'permissions': (('can_post', 'Can author blog posts'),)},
        ),
    ]
