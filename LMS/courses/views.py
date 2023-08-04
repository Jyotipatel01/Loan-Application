from django.shortcuts import render ,HttpResponse
from skops import io as sio
obj =sio.load('new.skops',trusted=True)
from courses.forms import loan_application_Form
#from sklearn.ensemble import RandomForestClassifier
#import sklearn
obj =sio.load('new.skops',trusted=True)
def get_name(request):
    
    if request.method == "POST":
        
        form= loan_application_Form(request.POST)
        if form.is_valid():
            gender = int(form.cleaned_data['Gender'])
            married = int(form.cleaned_data['Married'])
            dependents = int(form.cleaned_data['Dependents']) 
            education = int(form.cleaned_data['Education'])
            self_employee= int(form.cleaned_data['Self_Employed'])
            applicant_income = int(form.cleaned_data['ApplicantIncome'])
            coapplicantIncome = int(form.cleaned_data['CoapplicantIncome'])
            loanamount = int(form.cleaned_data['LoanAmount'])
            loanamountterm = int(form.cleaned_data['Loan_Amount_Term'])
            credithistory = int(form.cleaned_data['Credit_History'])
            property_area = int(form.cleaned_data['Property_Area'])
            result = obj.predict([[gender, married , dependents ,education, self_employee, applicant_income, coapplicantIncome, loanamount, loanamountterm, credithistory, property_area]])
            y = result[0]
            if y == 0:
                return HttpResponse("Thanks You !!! I am happy to say that you are eligible of loan")
            else:
                return HttpResponse("Thanks You !!! But we are regret to say the you are not eligible of loan")
                
            
            
    else:
        form = loan_application_Form()

    return render(request, "form.html", {"form": form})
# def ur(request):
#     return render(request,'jojo.html')
                  