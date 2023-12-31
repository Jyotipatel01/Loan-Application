# Generated by Django 4.2.2 on 2023-07-23 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_author_book_userprofile_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('Loan_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
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
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='books',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=34),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
