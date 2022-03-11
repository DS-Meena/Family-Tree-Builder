from django.shortcuts import render, redirect
from .models import individual
from .forms import IndividualForm
from .utils import *

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

	# create multiple trees
	trees = create_trees()

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
		curr = individuals.get(pk=pk)

		# check gender
		if new_individual.gender == 'M':
			curr.father = new_individual
		else:
			curr.mother = new_individual

		curr.save()

	return redirect('/create')








# def create_parent(request, pk):

# 	# request.method == 'POST':
# 	form = IndividualForm(request.POST, request.FILES)

# 	if form.is_valid():
# 		new_individual = form.save(commit=False)
# 		new_individual.save()

# 		# add the parent
# 		individuals = individual.objects.all()
# 		parent = individuals.get(pk=pk)

# 		# check gender
# 		if parent.gender == 'M':
# 			new_individual.father = individuals.get(pk=pk)
# 		else:
# 			new_individual.mother = individuals.get(pk=pk)

# 		new_individual.save()

# 	return redirect('/create')