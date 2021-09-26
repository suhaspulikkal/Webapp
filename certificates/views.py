from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Certificates


# Create your views here.

def certi(request):
    certs = Certificates.objects.all()
    if certs:
        return render(request, 'certi.html', {'certs': certs})
    else:
        messages.info(request, 'NO ACHIEVEMENTS ARE ADDED TO THE LIST')
    return render(request, 'certi.html')


def detail(request, id):
    det = Certificates.objects.get(pk=id)
    return render(request, 'detail.html', {'det': det})

