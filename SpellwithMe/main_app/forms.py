from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['date', 'minutes', 'numberofwords', 'adulthelp']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }