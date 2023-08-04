# Generated by Django 4.2.2 on 2023-08-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_loan_application_married_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_application',
            name='Credit_History',
            field=models.FloatField(choices=[('0', 'Yes'), ('1', 'No')]),
        ),
        migrations.AlterField(
            model_name='loan_application',
            name='Self_Employed',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=26),
        ),
    ]