from django.shortcuts import render, redirect
from .models import individual
from .forms import IndividualForm

# Create your views here.
def create(request):

	individuals = individual.objects.all()

	# if request is post, get details and save them
	if request.method == 'POST':
		form = IndividualForm(request.POST, request.FILES)

		if form.is_valid():
			new_individual = form.save(commit=False)
			new_individual.save()

		return redirect('/create')

	form = IndividualForm
	context = {
		'individuals': individuals,
		'form': form,
	}
	# print("Offsprings", individuals[0].offspring)
	return render(request, 'create.html', context)