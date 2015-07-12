from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length = 200)
	date = models.DateTimeField('date published', default=datetime.datetime.now,blank=True)
	description = models.TextField(default="Skill Description")
	resource = models.CharField(null=True, blank=True,max_length = 200)
	img = models.ImageField(null=True, blank=True)