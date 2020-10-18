from django.shortcuts import render

# Create your views here.

def productlist(request):
    return render(request, 'productlist.html')

def base(request):
    return render(request, 'base.html')