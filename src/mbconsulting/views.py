from django.http import HttpResponse
from django.shortcuts import render


def home_old(request):
    return render(request, "home.html")
