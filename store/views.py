from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from .models import Item, ItemDesc, User
from django.db import connection


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            email = form.cleaned_data['email']
            user_obj = User.objects.filter(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user_obj.exists():
                request.session['email'] = email
                request.session['first_name'] = user_obj.get().first_name
                request.session['id'] = user_obj.get().u_id
                return render(request, 'store/index.html', {'first_name': request.session['first_name']})

            return render(request, 'store/form.html', {'form': form, 'email': email})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'store/login.html', {'form': form})


def index(request):
    return render(request, 'store/index.html', {})


def profile(request):
    return HttpResponse("Hello, world. You're at the polls proiule.")


def home(request):
    return HttpResponse("Hello, world. You're at the polls home.")


def products(request):
    return render(request, 'store/products.html', {})


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']
            user_obj = User.objects.filter(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user_obj.exists():
                error = "Account with given Email ID already exists"
                return render(request, 'store/register.html', {'error': error})
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            request.session['email'] = email
            request.session['username'] = user_obj.get().first_name
            request.session['id'] = user_obj.get().u_id
            return render(request, 'store/index.html', {'username': request.session['username']})

        return render(request, 'store/form.html', {'form': form, })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'store/login.html', {'form': form})
    return render(request, 'store/register.html', {})


def search(request):
    return HttpResponse("Hello, world. You're at the polls search.")


def display(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM store_item')
    item = cursor.fetchone()
    id = item[2]
    cursor.execute('SELECT * FROM store_itemdesc where item_desc_id = %s', [id])
    itemdesc = cursor.fetchone()

    return render(request, 'store/display.html', {'item': item, 'itemdesc': itemdesc})
