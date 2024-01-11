from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse


# Create your views here.
def NewSchool(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        ESDO=SchoolForm(request.POST)
        if ESDO.is_valid():
            sn=ESDO.cleaned_data['sname']
            sp=ESDO.cleaned_data['sprincipal']
            sl=ESDO.cleaned_data['sloc']
            Se=ESDO.cleaned_data['Semail']
            Sr=ESDO.cleaned_data['SreenterEmail']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,SLocation=sl,Semali=Se,SreenterEmail=Sr)[0]
            SO.save()
            return HttpResponse('Data inserted')

    return render (request,'NewSchool.html',d)
