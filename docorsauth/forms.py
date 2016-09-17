from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import docorsUser

class docorsUserCreationForm(forms.ModelForm):
	#So you want to create a new human(user), well fulfill all my requirements first then the lord will consider

	error_messages = {
		'duplicate_email': _("A user with that email already exists."),
		'password_mismatch': _("The two password fields didn't match."),
	}

	password1 = forms.CharField(label=_('Create a Password'), widget=forms.PasswordInput)
	password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput, help_text=_("Enter the same password as above, for verification."))

	class Meta:
		model = get_user_model()
		fields = ['email','full_name']

	def clean_email(self):
		email = self.cleaned_data["email"]
		try:
			get_user_model()._default_manager.get(email=email)
		except get_user_model().DoesNotExist:
			return email
		raise forms.ValidationError(self.error_messages['duplicate_email'], code='duplicate_email',)

	def clean_password2(self):
		#you dare enter my chambers filthy and uncleaned, you shall be punished you weak human
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		#behold my creation. Feast your eyes with my greatness.
		user = super(docorsUserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password2'])
		if commit:
			user.save()
		return user

class docorsUserChangeForm(forms.ModelForm):
	#It is I who can change anything anytime. Your human weak eyes can witness the everything(password that is), so we have kept that hidden

	password = ReadOnlyPasswordHashField()

	class Meta:
		model = get_user_model()
		fields = ['email','password','full_name','is_active','is_admin']

	def clean_password(self):
		#Your eyes can't witness this so turn away as it may hurt(I know what you are thinking)
		return self.initial['password']