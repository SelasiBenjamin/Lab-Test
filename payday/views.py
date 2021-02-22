from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    payday = datetime.datetime.now()
    return render(request, "payday/index.html", {'payday': payday.day == 25 })