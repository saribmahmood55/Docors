from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import docorsUserCreationForm, docorsUserChangeForm
from .models import docorsUser

# The great lord admin have the control here Dont you dare defile any of his models(pun intended).hohhohohahahaha

class docorsUserAdmin(UserAdmin):
	#Witness my power, witness what I am capable of, witness you shall.
	form = docorsUserChangeForm
	add_form = docorsUserCreationForm

	list_display = ['email','full_name','is_doctor','is_admin']
	list_filter = ('is_admin','is_doctor','is_active',)
	fieldsets = (
		(None, {'fields':('email','password')}),
		('Personal Info', {'fields':('full_name','is_doctor',)}),
		('Status', {'fields':('is_active',)}),
		('Permissions', {'fields':('is_admin',)}),
	)

	add_fieldsets = (
		(None, {
				'classes':('wide',),
				'fields':('email','full_name','password1','password2','is_admin','is_doctor','is_active')
			}),
	)

	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(docorsUser,docorsUserAdmin)
#I work alone and dont need any group, I have all the power.
admin.site.unregister(Group)