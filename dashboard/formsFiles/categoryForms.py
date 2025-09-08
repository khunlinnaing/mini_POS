from django import forms
from ..models import Category


class CategoryForm(forms.ModelForm):  # For creating
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category description',
                'rows': 3,
            }),
        }

class EditCategoryForm(CategoryForm):  # For editing, inherits everything from CategoryForm
    pass