from django import forms
from .models import *

class myForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
