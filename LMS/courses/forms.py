from django import forms
from .models import loan_application


class loan_application_Form(forms.ModelForm):
    class Meta:
        model=loan_application
        fields='__all__'
        