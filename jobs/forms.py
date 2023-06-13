
from django import forms
from .models import Call
from django.forms import ModelForm


  
# create a ModelForm
class ContactForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Call
        fields = "__all__"


def clean(self):
    cleaned_data = super(ContactForm, self).clean()
    name = cleaned_data.get('name')
    email = cleaned_data.get('email')
    message = cleaned_data.get('message')
    if not name and not email and not  message:
        raise forms.ValidationError('You have to write something!')