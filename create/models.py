from django.db import models

# Create your models here.

# create a class to store individuals info
class individual(models.Model):
	first_Name = models.CharField(max_length = 100)
	last_Name = models.CharField(max_length = 100)

	def __str__(self):
		return self.first_Name;