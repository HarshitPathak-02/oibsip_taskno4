from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')

def homePage (request) :
    return render(request,"homepage.html")

def signupPage (request):
    if (request.method == 'POST'):
        try:
            uname = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            conpass = request.POST.get('confirm-password')

            if (password!=conpass):
                return HttpResponse("Please confirm your password correctly!")
        
            my_user = User.objects.create_user(uname,email,password)
            my_user.save()
        
            return redirect('signin')
        except Exception as e :
            return HttpResponse('You are already registered with us! Go to the login page.')
    

    return render(request,'signup.html')

def signinPage (request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Email or password is incorrect!")

    return render(request,"signin.html")