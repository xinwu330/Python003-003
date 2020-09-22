from django.shortcuts import render
from .models import Review

# Create your views here.
from django.http import HttpResponse
def index(request):
    reviews = Review.objects.all()
    return render(request, './frontend/index.html', locals())