from django.db import models

# Create your models here.

# create a class to store individuals info
class individual(models.Model):
	first_Name = models.CharField(max_length = 100)
	last_Name = models.CharField(max_length = 100)
	# # dob = models.DateField()

	offspring = models.ManyToManyField('self', null=True, blank=True, related_name='offsprings', symmetrical=False)
	parent = models.ManyToManyField('self', null=True, blank=True, related_name='parents', symmetrical=False)

	def __str__(self):
		return self.first_Name;
