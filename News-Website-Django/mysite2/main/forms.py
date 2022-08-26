from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserPreferenceForm


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

DIFFERENT_CATEGORIES = [
	('politics', 'Politics'),
	('covid-19', 'Covid-19'),
	('trending', 'Trending'),
	('international stories', 'International stories'),
	('independent sources', 'Independent Sources'),
	('sports', 'Sports'),
	('war in ukraine', 'War in Ukraine'),
]

class PreferenceForm(forms.ModelForm):

	class Meta:
		model = UserPreferenceForm
		fields = ['title']