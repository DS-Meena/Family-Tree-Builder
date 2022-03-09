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
	# print("Offsprings", individuals[0].id)
	return render(request, 'create.html', context)

def create_parent(request, pk):

	# request.method == 'POST':
	form = IndividualForm(request.POST, request.FILES)

	if form.is_valid():
		new_individual = form.save(commit=False)

		new_individual.save()

		# add the parent
		individuals = individual.objects.all()

		print(individuals)
		print(pk)
		new_individual.parent = individuals.get(pk=pk)
		new_individual.save()


	return redirect('/create')