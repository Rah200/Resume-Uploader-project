from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male', 'Male'), ('Female', 'Female')
]

JOB_CITY_CHOICES = [
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Banglore', 'Banglore'),
    ('Pune', 'Pune'),
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label='Preferred Job Locations', choices=JOB_CITY_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin',
                  'state', 'phone', 'email', 'job_city', 'profile_image', 'my_file']

        labels = {'name': 'Full name', 'dob': 'Date of Birth', 'pin': 'Pin Code',
                  'phone': 'Mobile No.', 'email': 'Email Id', 'profile_image': 'Profile Image', 'my_file': 'Document'}

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
                   'locality': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'pin': forms.NumberInput(attrs={'class': 'form-control'}),
                   'state': forms.Select(attrs={'class': 'form-select'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   }
