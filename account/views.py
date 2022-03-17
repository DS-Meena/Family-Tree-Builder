from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
# got user account page 
from django.conf import settings

from account.forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.

# to register a user
def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')

			print(email, raw_password)

			account = authenticate(email=email, password=raw_password)
			
			print(account)
			login(request, account)
			
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	# destination = get_redirect_if_exists(request)
	# print("destination: " + str(destination))

	if request.POST:
		print("post")

		form = AccountAuthenticationForm(request.POST)

		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			print(email, password, user)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect("home")

	else:

		form = AccountAuthenticationForm()
		print("here")

	context['login_form'] = form

	return render(request, "account/login.html", context)

# redirect to next page
def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect