from django.db import models
from django.forms import ModelForm
from django import forms


# Create your models here.
class Job01(models.Model):
    header = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=300)
    url = models.URLField()

class Job02(models.Model):
    id = models.BigAutoField(primary_key=True)
    # the rest of your fields go here

class Call(models.Model):
    name = models.CharField(max_length=200)
 #   phone = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=300)
    # Create your models here.

class ContactForm(ModelForm):
    class Meta:
       model = Call
       fields = '__all__'

    widgets = { 
            'name':forms.TextInput( attrs={  'class': 'form-control', 'required placeholder': 'Name', 'required': True } ),
            'email':forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Email', 'required': True}),
            'message':forms.Textarea( attrs={  'class': 'form-control', 'placeholder': 'Message', 'required': True}),
       
        }



    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.name
