from django.shortcuts import render, get_object_or_404
from .models import Job
from .forms import ContactForm

def home(request):
    return render(request, 'jobs/home.html',)

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})


def contact_view(request):
        
    # create object of form
        form = ContactForm(request.POST)
        
    # check if form data is valid
        if form.is_valid():
        # save the form data to model
            form.save()
            note="You message has been submitted!Thank you!"

        else: 
            note="I am very happy to get a message from you!"

        form = ContactForm()    
        return render(request, 'jobs/contact.html', {'form':form, 'note':note})

