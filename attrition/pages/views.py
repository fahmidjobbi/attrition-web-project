from django.shortcuts import render
from django.views.generic import TemplateView
import joblib as joblib

 
def home(request):
    context={}
    return render(request, 'index.html', context)

 
def analyze(request):
    context={}
    return render(request, 'analyze.html', context)
       
    

def about(request):
    context={}
    return render(request, 'about.html', context)


def result(request):
    
    cls=joblib.load('newmodel.sav')
    lis=[]
    lis.append(request.GET['OverTime'])
    lis.append(request.GET['Companyculture'])
    lis.append(request.GET['Worktimingsatisfaction'])
    lis.append(request.GET['Salaryandbenefit'])
    lis.append(request.GET['Skilldevelopment'])
    lis.append(request.GET['Worksatisfaction'])
    lis.append(request.GET['YerasAtCompany'])
    lis.append(request.GET['Worklifebalance'])
    lis.append(request.GET['Careergrowth'])

    print(lis)
    
    pred=cls.predict([lis])
      #pred is the predicted value
            
            
    return render(request, 'result.html', {'result':pred})




def team(request):
    context={}
    return render(request, 'team.html', context)

def contacte(request):
    context={}
    return render(request, 'contacte.html', context)
