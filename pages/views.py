from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Team 
from .models import Fitpicture 
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

#from .models import Picture




def home(request):
    teams = Team.objects.all()
    all_fitpictures = Fitpicture.objects.order_by('-created_date')
    data = {
        'teams': teams, 
        'all_fitpictures': all_fitpictures,
    }
    return render(request, 'home.html', data)




def about(request):
    teams = Team.objects.all()
    
    data = {
        'teams': teams, 
        
    }
    return render(request, 'about.html', data)

def services(request):
    teams = Team.objects.all()
    data = {
        'teams': teams, 
    }
    return render(request, 'services.html', data)

def galery(request):
    return render(request, 'galery.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        email_subject = 'You have a new message from Playgroundbroward' + subject
        
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Subject: ' + subject + '. Message: ' + message 
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email 
        
        send_mail(
            email_subject, 
            message_body, 
            'familytrain24@gmail.com',
            [admin_email], 
            fail_silently=False,
            )
        
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    return render(request, 'contact.html')


