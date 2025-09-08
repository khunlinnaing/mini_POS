from django import forms
from ..models import Table


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_number', 'capacity', 'is_occupied']
        widgets = {
            'table_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ဥပမာ - A1',
                'required': 'required'
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ဥပမာ - 4',
                'required': 'required',
                'min': 1
            }),
            'is_occupied': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class EditTableForm(TableForm):
    pass  # Optionally override __init__ if needed later
