from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .decorators import *
from .models import *

@unauthentucated_user
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Username or password is incorrect')
    context = {}
    return render(request,'agroia/index.html',context)

def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def dashboard(request):
    context = {}
    return render(request,'agroia/dashboard.html',context)

@login_required(login_url='index')
@allowed_users(allow_roles=['Administrator'])
def users(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('role')
            group = Group.objects.get(name=role)
            user.groups.add(group)
            messages.info(request, 'Acconunt was created for ' + username )
            return redirect('users')
    users = User.objects.exclude(username=request.user.username).exclude(is_superuser=True)
    context = {'users':users,'form':form}
    return render(request, 'agroia/users.html',context)


@login_required(login_url='index')
@allowed_users(allow_roles=['Administrator'])
def user_update(request,pk_t):
    try:
        person = User.objects.exclude(is_superuser=True).get(id = pk_t)
        if request.method == "GET":
            form = UserChangeForm(instance = person)
            context = {'person':person,'form':form}
            return render(request, 'agroia/user_update.html',context)
        else:
            form = UserChangeForm(request.POST, instance = person)
            if form.is_valid():
                oldGroup = person.groups.all()[0].name
                group = Group.objects.get(name=oldGroup)
                person.groups.remove(group)
                role = form.cleaned_data.get('role')
                group = Group.objects.get(name=role)
                person.groups.add(group)
                form.save()
                messages.info(request, 'Acconunt ' + person.username + " was update")
    except:
        messages.error(request, 'Can not edit this user')
    return redirect('users')


@login_required(login_url='index')
@allowed_users(allow_roles=['Administrator'])
def user_delete(request,pk_t):
    try:
        person = User.objects.exclude(is_superuser=True).get(id = pk_t)
        messages.info(request, 'Acconunt ' + person.username + " was deleted")
        person.delete()
    except:
        messages.error(request, 'Can not delete this user')
    return redirect('users')

@login_required(login_url='index')
def estimate(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.create_by=request.user.id
            id_method = form.cleaned_data.get('method')
            item.method= id_method
            item.save()
            pk = item.id
            return redirect('result',pk)
    methods = Method.objects.all()
    context = {'form':form,'methods':methods}
    return render(request,'agroia/estimate.html',context)

@login_required(login_url='index')
def result(request,pk_t):
    try:
        item = Item.objects.get(id = pk_t)
    except:
        messages.error(request, 'No results found')
    context = {'item':item}
    return render(request,'agroia/result.html',context)

@login_required(login_url='index')
def files(request):
    items = Item.objects.filter(upload_by=request.user.id)
    context = {'items':items}
    return render(request, 'agroia/files.html',context)


@login_required(login_url='index')
def method(request):
    context = {}
    return render(request,'agroia/method.html',context)
