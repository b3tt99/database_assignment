from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Client


def index_page(request):
    data = Client.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def login_page(request):
    return render(request, "login.html")


def edit_page(request):
    return render(request, "edit.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        query = Client(name=name, email=email, age=age, gender=gender, country=country, city=city)
        query.save()
        return redirect("/")

        return render(request, 'index.html')


def deleteData(request, id):
    d = Client.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        # Receive updated data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        city = request.POST.get("city")

        # update the product
        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.gender = gender
        update_info.country = country
        update_info.city = city

        # Return the updated value back to the database
        update_info.save()
        return redirect("/")

    d = Client.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)