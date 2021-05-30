import json
import requests
from django.shortcuts import render
from cardapi.models import Card

def getTheAPIData(id):
    url = f"http://127.0.0.1:8000/api/{id}"
    requests.request("GET", url)



def provideCardDetails(request):
    context={}

    if request.method == "GET":
        context['f'] = False
    elif request.method == "POST":
        val = request.POST.get("cardnum")
        getTheAPIData(val)
        context['f'] = True
        context['data'] = Card.objects.get(number=val)

    return render(request,'index.html',context)