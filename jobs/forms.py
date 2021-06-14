
from .models import Call
from django.forms import ModelForm

  
# create a ModelForm
class ContactForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = Call
        fields = "__all__"