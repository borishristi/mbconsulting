from django.http import HttpResponse
from django.shortcuts import render


def home_old(request):
    # return render(request, "home.html")
    return HttpResponse("<h1>c'est bon<h1>")

