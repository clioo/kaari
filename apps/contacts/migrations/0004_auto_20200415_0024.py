# Generated by Django 2.2.2 on 2020-04-15 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20200414_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.AddField(
            model_name='ourlistinginterest',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
