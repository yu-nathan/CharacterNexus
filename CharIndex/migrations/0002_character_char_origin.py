# Generated by Django 2.2.6 on 2019-10-26 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charIndex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='char_origin',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]