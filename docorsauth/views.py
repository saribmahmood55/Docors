from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import login

from .forms import docorsUserCreationForm

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = docorsUserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
	else:
		form = docorsUserCreationForm()
	print form
	return render(request, "registration/registration_form.html", {'form': form})

def custom_login(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
	else:
		return login(request)