from django.shortcuts import render
from .models import Entry
from django.shortcuts import get_object_or_404, render

def blog(request):
	blogentries = Entry.objects.all()
	context = {'blogentries':blogentries}
	return render(request, 'blog/blog.html',context)

