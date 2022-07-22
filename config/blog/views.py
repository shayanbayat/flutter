from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return HttpResponse("helooooo")

def api(request):
    data = {
        'title':'ringLight hart',
        'img':'1.jpg',
        'price':'10000'
    }

    return JsonResponse(data)