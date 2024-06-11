from django.shortcuts import render,redirect
from transformers import pipeline
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from cProfile import Profile
from django.shortcuts import redirect , render
from app.emailbackend import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

def home(request):
    if request.method=='POST':
        input_text = request.POST.get('input_text')
        summarizer_ans = summarizer(input_text,max_length=100, min_length=20,do_sample=False)[0]['summary_text']
        return render(request,'index.html',{'summarizer_ans':summarizer_ans})
    return render(request,'index.html')

def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
    #check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('register')
    
    #check username
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username already Exists')
            return redirect('register')
    
        user = User(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'registration/register.html')



def dologin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
		
        user = EmailBackEnd.authenticate(request,username=email,password=password)
        if user!=None:
           login(request,user)
           return redirect('home')
        else:
           messages.warning(request,'Email and Password Are Invalid !')
           return redirect('login')
    return render(request,'registration/login.html')
 
def homepage(request):
     return render(request,'homepage.html')