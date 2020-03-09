from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings" : Meeting.objects.count()})

def date(request):
    HttpResponse("This page was served at " + str(datetime.now()))
