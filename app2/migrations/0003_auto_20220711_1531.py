# Generated by Django 3.0 on 2022-07-11 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_auto_20220711_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_delete',
            new_name='is_active',
        ),
    ]
