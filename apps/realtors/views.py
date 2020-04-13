from django.shortcuts import render
from apps.realtors.models import Realtor
# Create your views here.

def realtors_view(request):
    return render(request,'realtors/realtors.html',{
        'realtors':Realtor.objects.filter(status=True) #Active users
    })

def get_realtor_view(request,nombre):
    return render(request,'realtors/realtor.html',{
        'realtor':Realtor.objects.get(shortName=nombre) #Active users
    })
