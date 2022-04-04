from django.shortcuts import render
from django.views.generic import TemplateView


 
def home(request):
    context={}
    return render(request, 'index.html', context)

 
def analyze(request):
    context={}
    return render(request, 'analyze.html', context)
       
    

def about(request):
    context={}
    return render(request, 'about.html', context)



def team(request):
    context={}
    return render(request, 'team.html', context)

def contacte(request):
    context={}
    return render(request, 'contacte.html', context)
