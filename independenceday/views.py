from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "independence/index.html", {
        "independenceday": now.month == 3 and now.day == 6
    })