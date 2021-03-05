from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "republic/index.html", 
    {"republic": now.month == 7 and now.day == 1 
    })
