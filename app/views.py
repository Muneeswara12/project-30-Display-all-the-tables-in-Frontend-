from django.shortcuts import render

from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Topic is created')

def insert_webpage(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    n=input('enter player name:')
    u=input('enter url:')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()

    return HttpResponse('webpage is created')

def insert_access_record(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    n=input('enter player name:')
    u=input('enter url:')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()

    d=input('enter date like yyyy-mm-dd:')
    a=input('enter author name:')
    aro=AccessRecord.objects.get_or_create(name=wo,date=d,auther=a)[0]
    aro.save()

    return HttpResponse('access record is created')

def display_topic(request):
    tpo=Topic.objects.all()
    d={'tpo':tpo}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    wpo=Webpage.objects.all()
    d1={'webpage':wpo}
    return render(request,'display_webpage.html',d1)

def display_accessrecord(request):
    aro=AccessRecord.objects.all()
    d2={'accessrecord':aro}
    return render(request,'display_accessrecord.html',d2)

def display_db(request):
    tpo=Topic.objects.all()
    wpo=Webpage.objects.all()
    aro=AccessRecord.objects.all()
    d={'to':tpo,'wo':wpo,'ao':aro}
    return render(request,'display_all.html',d)
