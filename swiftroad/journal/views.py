from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Super Basic Index brah."""
    return HttpResponse("Hello, World. This is a django app mkay...")