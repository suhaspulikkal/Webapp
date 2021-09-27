from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from register.models import Emails


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        check = [first_name,last_name,username,password2,password1,email]
        for a in check:


            if a=='':
             messages.info(request,"EMPTY FIELDS |  UNSUCCESSFULL")
             return redirect('register')
             endfor

        if password1!=password2:

            messages.info(request,"PASSWORD MISMATCH |  UNSUCCESSFULL")

            return redirect('register')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USER NAME ALREADY TAKEN |  UNSUCCESSFULL")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"EMAIL ID ALREADY EXIST |  UNSUCCESSFULL")
                return redirect('register')
            else:


                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                user.save();
                messages.info(request,'REGISTRATION SUCESSFULL')

            return redirect('login')

    return render(request,'register.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:

        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def main(request):

    return render(request,'main.html')

def base(request):

    return render(request,'base.html')

def home(request):

    return render(request,'home.html')

def datas(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request,'data.html',{'users':users})

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        subject = request.POST['subject']
        print('DATA STORED SUCCESSFULLY')
        send_mail(subject, message, 'pulikkalsuhas@gmail.com','suhasps05@gmail.com',fail_silently=False)
        messages.info(request,'EMAIL SENT')
    return render(request,'contact.html')
