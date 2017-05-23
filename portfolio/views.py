from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from portfolio.forms import ContactForm
from contact_form.models import details
import datetime

def index(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'about_me.html')

'''def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/message/')
    else:
        form = ContactForm()
    return render(request, 'message.html')'''

def message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            now = datetime.datetime.now()
            data = details.objects.create(subject=cd['subject'], email=cd['email'], message=cd['message'], name=cd['name'], date=now)  
            return HttpResponseRedirect('/message/thanks/')
    else:
        form = ContactForm()
    messages = details.objects.order_by("-date")
    return render(request, 'message.html', { 'messages': messages, 'form': form })

def message_thanks(request):
    messages = details.objects.order_by("-date")
    return render(request, 'message_thanks.html', { 'messages': messages })

