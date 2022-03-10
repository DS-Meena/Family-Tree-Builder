from django import forms
from django.forms import ModelForm
from .models import individual

# create individual form
class IndividualForm(ModelForm):
	class Meta:
		model = individual
		fields = ['first_Name', 'last_Name', 'gender']

		labels = {
			'first_Name': 'First Name',
			'last_Name': 'Last Name',
			'gender': 'Gender',
		}

		widgets = {
			'first_Name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'last_Name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			'gender': forms.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
		}