from django.shortcuts import render
from .models import Entry
from django.shortcuts import get_object_or_404, render

def skills(request):
	skillentries = Entry.objects.all()
	context = {'skillentries':skillentries}
	return render(request, 'skills/skills.html',context)

