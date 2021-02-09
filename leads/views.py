from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, "html/home_page.html")
