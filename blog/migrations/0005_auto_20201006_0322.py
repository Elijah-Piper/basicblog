# Generated by Django 3.1.2 on 2020-10-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201006_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]