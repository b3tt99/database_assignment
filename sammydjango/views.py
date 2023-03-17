from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Client


from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.shortcuts import render


def index_page(request):
    data = Client.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def edit_page(request):
    return render(request, "edit.html")

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        MID = request.POST.get('MID')
        DOI = request.POST.get('DOI')


        query = Client(name=name, email=email, MID=MID, DOI=DOI)
        query.save()
        return redirect("/")

        return render(request, 'home.html')


def deleteData(request, id):
    d = Client.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "home.html")


def updateData(request, id):
    if request.method == "POST":
        # Receive updated data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        MID = request.POST.get("MID")
        DOI = request.POST.get("DOI")


        # update the product
        update_info = Client.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.MID = MID
        update_info.DOI = DOI


        # Return the updated value back to the database
        update_info.save()
        return redirect("/")

    d = Client.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)


def pay(request, id):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'SAMANTHA'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'payments.html')
