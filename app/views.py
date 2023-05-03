from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

def three(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessRecordForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}

    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessRecordForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            NSTFO=tfd.save(commit=False)
            NSTFO.save()


            NSWFO=wfd.save(commit=False)
            NSWFO.topic_name=NSTFO
            NSWFO.save()


            NSAFO=afd.save(commit=False)
            NSAFO.name=NSWFO
            NSAFO.save()
            return HttpResponse('excution is succesfully')
        else:
            return HttpResponse('not valid')
           

























    return render(request,'three.html',d)