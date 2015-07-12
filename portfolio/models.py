from django.db import models

# Create your models here.
# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length = 200)
	date = models.DateTimeField(max_length= 200, null=True, blank=True)
	resource = models.CharField(max_length = 200,null=True, blank=True)
	img = models.ImageField(null=True, blank=True)
	description = models.TextField(default="Project description")