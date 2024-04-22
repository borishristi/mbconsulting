from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render


def home_view(request):
    return render(request, "mbsite/index.html")
    # return HttpResponse("<h1>TEST</h1>")


def contact_view(request):
    return render(request, "mbsite/contact.html")


def service_view(request):
    return render(request, "mbsite/service.html")


def about_view(request):
    return render(request, "mbsite/about.html")


def project_view(request):
    return render(request, "mbsite/project.html")


def feature_view(request):
    return render(request, "mbsite/feature.html")


def quote_view(request):
    return render(request, "mbsite/quote.html")


def team_view(request):
    return render(request, "mbsite/team.html")


def testimonial_view(request):
    return render(request, "mbsite/testimonial.html")


def error_404_view(request):
    return render(request, "mbsite/404.html")
