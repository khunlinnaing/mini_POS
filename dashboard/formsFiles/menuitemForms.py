from django import forms
from ..models import Item




class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category', 'is_available', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ဥပမာ - ကော်ဖီ',
                'required': 'required'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'အသားပေးဖော်ပြချက်...',
                'rows': 3
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ဥပမာ - 1500.00',
                'required': 'required'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class EditMenuItemForm(MenuItemForm):
    """Same as MenuItemForm but image field is not required during update."""
    def __init__(self, *args, **kwargs):
        super(EditMenuItemForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
