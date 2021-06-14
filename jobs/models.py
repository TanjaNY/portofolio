from django.db import models
from django.forms import ModelForm


# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=300)
    url = models.URLField()

class Call(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    message = models.TextField(max_length=400)
    # Create your models here.

class ContactForm(ModelForm):
    class Meta:
       model = Call
       fields = '__all__'


    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.name
