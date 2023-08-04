from django.db import models
class loan_application(models.Model):
    Married = models.CharField(max_length=10 , choices=[('1' , 'Yes'),('0' , 'No' )] , default=None)
    Gender = models.CharField(max_length=10 , choices=[('1' , 'MALE'),('0' , 'FEMALE' )])
    Dependents = models.CharField(max_length=50,choices=[('0' , '0'),('1' , '1'),('2','2'),('3','3')])
    Education = models.CharField(max_length=20,choices=[('0' , 'Graduate'),('1' , 'Not Graduate')] )
    Self_Employed = models.CharField(max_length=26,choices=[('1' , 'Yes'),('0' , 'No')]) 
    ApplicantIncome = models.FloatField()
    CoapplicantIncome = models.FloatField()
    LoanAmount = models.FloatField()
    Loan_Amount_Term = models.IntegerField()
    Credit_History = models.FloatField(choices=[(1,"Yes"),(0,"No")])
    Property_Area = models.CharField(max_length=50,choices=[('0' , 'Rural 	'),('1' , 'Semiurban'),('2','Urban')])
    