from django.db import models

# Create your models here.
# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length = 200)
	date = models.DateTimeField(max_length= 200)
	resource = models.CharField(max_length = 200)
	read = models.BooleanField()
	img = models.ImageField()