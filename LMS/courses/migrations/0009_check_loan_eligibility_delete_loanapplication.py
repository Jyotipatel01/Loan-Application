# Generated by Django 4.2.2 on 2023-07-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_loanapplication_remove_book_author_remove_tag_books_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_loan_eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=10)),
                ('Married', models.CharField(max_length=20)),
                ('Dependents', models.CharField(max_length=50)),
                ('Education', models.CharField(max_length=20)),
                ('Self_Employed', models.CharField(max_length=26)),
                ('ApplicantIncome', models.FloatField()),
                ('CoapplicantIncome', models.FloatField()),
                ('LoanAmount', models.FloatField()),
                ('Loan_Amount_Term', models.IntegerField()),
                ('Credit_History', models.FloatField()),
                ('Property_Area', models.CharField(max_length=50)),
                ('Loan_Status', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='LoanApplication',
        ),
    ]
