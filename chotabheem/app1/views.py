from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    hey = "HEY SIRI"
    apple = "google's frind"
    return HttpResponse(f"{hey} <br> {apple}")