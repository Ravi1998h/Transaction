from django import forms
from django.db.models import fields
from django.forms.forms import Form
from .models import user

class userform(forms.ModelForm):
    class Meta:
        model = user
        fields='__all__'

class depo(forms.Form):
    depo_by=forms.CharField(max_length=100)
    depo_to=forms.CharField(max_length=100)
    depo_amt=forms.IntegerField()