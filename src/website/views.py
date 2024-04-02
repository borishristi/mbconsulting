from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(request, "website/index.html")
    # return HttpResponse("<h1>TEST</h1>")