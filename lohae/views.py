from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def productlist(request):
    return render(request, 'productlist.html')

def buy_item(request):
    return render(request, 'buy_item.html')
