# Generated by Django 4.2.2 on 2023-07-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_loan_application_married'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_application',
            name='Property_Area',
            field=models.CharField(choices=[('MALE', 0), ('FEMALE', 1)], max_length=50),
        ),
    ]
