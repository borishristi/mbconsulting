from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(request, "website/index.html")
    # return HttpResponse("<h1>TEST</h1>")


def contact_view(request):
    return render(request, "website/contact.html")


def service_view(request):
    return render(request, "website/service.html")


def about_view(request):
    return render(request, "website/about.html")


def project_view(request):
    return render(request, "website/project.html")


def feature_view(request):
    return render(request, "website/feature.html")


def quote_view(request):
    return render(request, "website/quote.html")


def team_view(request):
    return render(request, "website/team.html")


def testimonial_view(request):
    return render(request, "website/testimonial.html")


def error_404_view(request):
    return render(request, "website/404.html")
