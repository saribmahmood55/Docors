from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import login
from .utility import send_activation_link
from .models import EmailConfirmation

from patients.forms import CreatePatient
from .forms import docorsUserCreationForm

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = CreatePatient(request.POST)
		if form.is_valid():
			new_user = form.save()
			send_activation_link(new_user)
			return render(request, "registration/registration_complete.html", {'registered_user': new_user})
	else:
		form = CreatePatient()
	return render(request, "registration/registration_form.html", {'form': form})

def activate(request, token):
	email_confirm = EmailConfirmation.objects.get(key=token)
	data = email_confirm.confirm_activation()
	return render(request, "registration/activate.html", {'data':data})

def custom_login(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
	else:
		return login(request)