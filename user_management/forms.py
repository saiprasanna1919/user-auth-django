from django import forms
from django.contrib.auth import get_user_model
from .models import Blog

User = get_user_model()

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password', 'role', 'profile_picture',
                  'address_line1', 'city', 'state', 'zip_code']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

class PatientRegistrationForm(DoctorRegistrationForm):
    class Meta:
        model = User
        fields = DoctorRegistrationForm.Meta.fields.copy()
        fields.remove('role')  # Patients can't choose a role

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']