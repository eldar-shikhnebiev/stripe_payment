
# Create your views here.
from django.shortcuts import render


def go_to_homepage(request):

    return render(request, 'index.html')