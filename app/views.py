from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *
def htmlform(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST.get('pw')

        return HttpResponse('Submitted')
    return render(request,'htmlform.html')

def create_school(request):
    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST['sl']
        pr=request.POST['pr']

        SO=School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=pr)[0]
        SO.save()

        #return HttpResponse('School is created')
        QLSO=School.objects.all()
        d={'schools':QLSO}
        return render(request,'display_school.html',d)

    return render(request,'create_school.html')