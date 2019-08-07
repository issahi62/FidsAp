from django.db import models

# Create your models here.
class Costumer(models.Model):
	"""docstring for Costumer_Name"""
	Student_Name = models.CharField(max_length = 250)
	Address = models.CharField(max_length = 250)
	Contacts = models.FloatField(max_length = 250)
	Moving_Date= models.CharField(max_length = 250)
		
class item(models.Model):

    itemation = models.ForeignKey(Costumer, on_delete=models.CASCADE)

    funiture = models.CharField(max_length = 200)
    shoes = models.CharField(max_length = 200)
    clothes = models.CharField(max_length = 200)
    