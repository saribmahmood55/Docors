from django import forms
from patients.models import Patient
from django.utils.translation import ugettext_lazy as _

class CreatePatient(forms.ModelForm):

	error_messages = {
		'duplicate_email': _("A user with that email already exists."),
		'password_mismatch': _("The two password fields didn't match."),
	}

	password1 = forms.CharField(label=_('Create a Password'), widget=forms.PasswordInput)
	password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput, help_text=_("Enter the same password as above, for verification."))

	class Meta:
		model = Patient
		fields = ['email','full_name']

	def clean_email(self):
		email = self.cleaned_data["email"]
		try:
			Patient.objects.get(email=email)
		except Patient.DoesNotExist:
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
		user = super(CreatePatient, self).save(commit=False)
		user.set_password(self.cleaned_data['password2'])
		if commit:
			user.save()
		return user