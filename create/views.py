from django.shortcuts import render, redirect
from .models import individual

# Create your views here.
def create(request):

	individuals = individual.objects.all()

	# if request is post, get details and save them
	if request.method == 'POST':

		new_individual = individual(
				first_Name = request.POST['first_name'],
				last_Name = request.POST['last_name']
			)
		new_individual.save()

		return redirect('/create')

	context = {
		'individuals': individuals
	}

	return render(request, 'create.html', context)