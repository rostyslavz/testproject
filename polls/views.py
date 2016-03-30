from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

def home(request):
	context = {
		"title": "Home page"
	}
	return render(request,'homecontent.html', context)