from django import forms
from django.forms import ModelForm
from .models import NewsLetterRecipients

class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetterRecipients
        fields = ('name', 'email')

        # labels={

        #   'name': '',
        #    'email': '',
          
        # }

        widgets = {
           'name' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}),
           'email' :forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email Address'}),

        }
   