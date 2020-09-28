from django.shortcuts import render
from .models import Review

# Create your views here.
from django.http import HttpResponse
def index(request):
    reviews = Review.objects.all()
    q = request.GET.get('q')
    print("----------------------------------")
    print(q)
    print("----------------------------------")
    return render(request, './frontend/index.html', locals())