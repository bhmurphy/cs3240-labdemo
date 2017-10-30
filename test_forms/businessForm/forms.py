from django import forms

from django.core.exceptions import ValidationError

class businessForm(forms.Form):
    name = forms.CharField(max_length=50)
    mission_statement = forms.CharField(max_length=1000)
    incorpDate = forms.DateField(required=False)
    files = forms.FileField(required=False)

