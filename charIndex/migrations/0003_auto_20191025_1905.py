# Generated by Django 2.2.6 on 2019-10-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charIndex', '0002_character_char_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='range',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='stats',
            name='super_range',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
