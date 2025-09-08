from django import forms
from django.contrib.auth.models import User

from dashboard.widgets import input_widget
from ..models import UserProfile


class UserForm(forms.ModelForm):
    # Extra fields not on the User model
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password',
            'required': 'required',
        })
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password',
            'required': 'required',
        })
    )
    phone = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ဥပမာ: 09xxxxxxxxx',
            'required': 'required',
        })
    )
    profile = forms.ImageField(
        label="Profile Image",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
        })
    )
    staff_level = forms.ChoiceField(
        label="Staff Level",
        choices=UserProfile.STAFF_LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'confirm_password',
            'first_name', 'last_name', 'phone', 'profile', 'staff_level'
        ]
        
    username = forms.CharField(widget=input_widget(
        placeholder='ဥပမာ: aungaung',
        input_id='userName',
        required=True
    ))

    email = forms.EmailField(widget=input_widget(
        placeholder='ဥပမာ: example@gmail.com',
        required=True
    ))

    first_name = forms.CharField(widget=input_widget(
        placeholder='ဥပမာ: Aung',
        required=True
    ))

    last_name = forms.CharField(widget=input_widget(
        placeholder='ဥပမာ: Aung',
        required=True
    ))

    # rest of your form fields ...


    def clean(self):
        """Ensure password and confirm_password match."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        """Save both User and related UserProfile."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # hash password

        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone=self.cleaned_data.get('phone'),
                profile=self.cleaned_data.get('profile'),
                staff_level=self.cleaned_data.get('staff_level'),
            )
        return user


class EditUserForm(UserForm):
    """
    Edit form that inherits from UserForm but removes password and confirm_password fields.
    Used for updating existing users.
    """

    class Meta(UserForm.Meta):
        # Reuse the same fields minus password fields
        exclude = ['password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove password fields
        self.fields.pop('password', None)
        self.fields.pop('confirm_password', None)

        # Populate UserProfile fields
        if self.instance:
            try:
                profile = self.instance.profile
                self.fields['phone'].initial = profile.phone
                self.fields['profile'].initial = profile.profile
                self.fields['staff_level'].initial = profile.staff_level
            except UserProfile.DoesNotExist:
                pass  # Ignore if profile doesn't exist

    def save(self, commit=True):
        """Save User and update or create UserProfile."""
        user = super(UserForm, self).save(commit=False)  # Call grandparent

        if commit:
            user.save()

        try:
            profile_instance = user.profile
        except UserProfile.DoesNotExist:
            profile_instance = UserProfile(user=user)

        profile_instance.phone = self.cleaned_data.get('phone')
        profile_instance.profile = self.cleaned_data.get('profile')
        profile_instance.staff_level = self.cleaned_data.get('staff_level')

        if commit:
            profile_instance.save()

        return user
