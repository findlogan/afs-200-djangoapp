from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/userpanel')
        else:
            messages.info(request, 'Incorrect username or password!')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('User Created!')
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def store(request):
    return render(request, 'store.html')

def userpanel(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            imgURL = request.FILES['imgURL']
            desc = request.POST ['desc']
            Product.objects.create(name=name, imgURL=imgURL, desc=desc)
            products = Product.objects.all()
            return render(request, 'admin.html', {'products': products})
        else:
            products = Product.objects.all()
            return render(request, 'admin.html', {'products': products})
    else:
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')

def delete(request, the_id):
    if request.user.is_authenticated:
        Product.objects.get(id=the_id).delete()
        return redirect('/userpanel')
    else:
        return redirect('/login')