import datetime
from django.shortcuts import render, redirect, reverse
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout  
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login') 
def show_main(request):
    # Mengambil semua entri produk yang dimiliki oleh pengguna yang sedang login
    context = {
        'name': request.user.username,
        'class': 'PBP C',
        'npm': '2306275512',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    if request.method == 'POST':
        form = ProductEntryForm(request.POST, request.FILES)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')
    else:
        form = ProductEntryForm()
    return render(request, "create_product_entry.html", {'form': form})

def show_json(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Mengambil objek produk berdasarkan id
    product = ProductEntry.objects.get(pk=id)
    # Membuat form dengan instance produk yang akan diedit
    form = ProductEntryForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid() and request.method == "POST":
        # Menyimpan perubahan jika form valid dan metode request adalah POST
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    # Menampilkan form edit jika metode request bukan POST atau form tidak valid
    return render(request, "edit_product.html", {'form': form})

def delete_product(request, id):
    # Mengambil objek produk berdasarkan id
    product = ProductEntry.objects.get(pk = id)
    # Menghapus produk dari database
    product.delete()
    # Kembali ke halaman utama setelah penghapusan
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def add_product_entry_ajax(request):
    if request.method == 'POST':
        form = ProductEntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error"}, status=405)