from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from about.models import About


def about(request):

    aboutin=About.objects.all()
    if aboutin :
        return render(request, 'about.html', {'aboutin': aboutin})
    else:
        messages.info(request,'NO ABOUT DATA TO SHOW')
