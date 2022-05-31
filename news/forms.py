from django import forms
from django.forms import ModelForm
from .models import NewsLetterRecipients,Article

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

class NewArticleForm(forms.ModelForm):

    class Meta:
           model = Article
           exclude = ['editor', 'pub_date']
           widgets = {
            'tags': forms.CheckboxSelectMultiple(),
           }
   