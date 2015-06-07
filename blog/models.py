from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length = 200)
	date = models.DateTimeField('date published', default=datetime.datetime.now,blank=True)
	content = models.TextField()
	resource = models.CharField(null=True, blank=True,max_length = 200)
	read = models.BooleanField()
	img = models.ImageField(null=True, blank=True)