from django.shortcuts import render

# Create your views here.

def heather(request):
    return render(request, 'jobs/heather.html')

def home(request):
    return render(request, 'jobs/home.html')
