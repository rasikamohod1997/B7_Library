# Generated by Django 3.0 on 2022-07-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_auto_20220711_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
