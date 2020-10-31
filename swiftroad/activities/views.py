from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Super Basic Index brah."""
    return render(request, "activities/index.html", context={"title": "SwiftRoad"})
