# Generated by Django 4.2.2 on 2023-06-26 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='courses',
            new_name='course',
        ),
    ]