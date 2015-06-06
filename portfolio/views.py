from django.shortcuts import render
from .models import Entry
from django.shortcuts import get_object_or_404, render

def portentry(request):
	entries = Entry.objects.all()
	context = {'entries':entries}
	return render(request, 'portfolio/portfolio.html',context)