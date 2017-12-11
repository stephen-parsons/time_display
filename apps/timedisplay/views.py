from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
	context = {
	"time": strftime("%I:%M %p", localtime()),
	"date": strftime("%B %d, %Y", localtime())
	}
	return render(request,'timedisplay/index.html', context)
