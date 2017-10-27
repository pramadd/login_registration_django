from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request,'belt/index.html')

def success(request):
    context = {}
    context['stuff'] = User.objects.all()
    return render(request,'belt/success.html',context)

def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    x = {'first_name': first_name,'last_name': last_name, 'email': email, 'password': password, 'confirm_password': confirm_password}
    errors = User.objects.validate(x)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed_password )
        return redirect('/success')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    print "inside login"
    
    errors = User.objects.validateLogin(request.POST)
    print errors
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        print "redirecting to root"
        return redirect('/')
    else:
       return redirect('/success')




    

