from django import forms
from ..models import Company

class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_logo', 'company_address']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name',
                'required': 'required',
            }),
            'company_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Address',
                'required': 'required',
            }),
            'company_logo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
