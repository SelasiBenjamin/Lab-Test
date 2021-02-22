from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    repub_day = datetime.datetime.now()
    return render(request, "republic/index.html", {'Republic Day': repub_day.month == 7 and repub_day.day == 1 })