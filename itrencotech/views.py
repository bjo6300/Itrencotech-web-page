from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def index(request):
    return render(request, 'home.html')

def body_onlyIdea_onlyIdea(request):
    return render(request, 'body/onlyIdea/onlyIdea_home.html')

def body_prototyping_prototyping_home(request):
    return render(request, 'body/prototyping/prototyping_home.html')