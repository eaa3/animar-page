# Create your views here.
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse



def index(request):

	return render(request,'index.html')


