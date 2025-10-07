from dataclasses import fields
from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#   name=forms.CharField(max_length=100, label="Name")
#   email=forms.EmailField(max_length=100,label="Email" )

class ContactForm(forms.ModelForm):
  class Meta:
    model=Contact
    fields=["name", "email", "message"]
  