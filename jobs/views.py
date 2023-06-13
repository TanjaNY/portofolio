from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from .models import Job01
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse 


#class HomePageView(TemplateView):
    #template_name = 'jobs/home#slide01'



def port(request):
    jobs = Job01.objects
    return render(request, 'jobs/port.html',{'jobs':jobs})

    
def home(request):
    return render(request, 'jobs/home.html',)

def aboutme(request):
    return render(request, 'jobs/aboutme.html',) 

def services(request):
    return render(request, 'jobs/services.html',) 

def mywork(request):
    return render(request, 'jobs/mywork.html',) 

def detail(request, job_id):
    job_detail = get_object_or_404(Job01, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})



def contact_view(request):
    #form=ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        # if request is not post, initialize an empty form
            
        if form.is_valid(): 
            contact=form.save(commit=True)
            contact.save()        
            
            subject = "inquiry"
            body={            
            'name' : form.cleaned_data['name'],
            'email' : form.cleaned_data['email'],
            'message' : form.cleaned_data['message'],
            }

            message = "\n".join(body.values())
            
            try:
                 send_mail(subject, message, 'ta.nyberg@gmail.com', ['tanja.nyberg@outlook.com'],fail_silently=False)
            
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            else:
                return HttpResponse('Form is not authorized.')
    else:
        form=ContactForm()   
        return render(request, 'jobs/contact.html', {'form': form})

