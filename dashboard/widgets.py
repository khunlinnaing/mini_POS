from django import forms

def input_widget(placeholder, input_id=None, required=True):
    attrs = {
        'class': 'form-control',
        'placeholder': placeholder,
    }
    if input_id:
        attrs['id'] = input_id
    if required:
        attrs['required'] = 'required'
    return forms.TextInput(attrs=attrs)