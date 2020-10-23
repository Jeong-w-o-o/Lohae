from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_view
from .forms import CustomAuthenticationForm




# Create your views here.

def main(request):
    return render(request, 'main.html')

def productlist(request):
    return render(request, 'productlist.html')

def buy_item(request):
    return render(request, 'buy_item.html')

def write_messages(request):
    return render(request, 'write_messages.html')

def signup(request):
    regi_form = UserCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('main')
    return render(request, 'signup.html', {'regi_form':regi_form})

def login(request):
    return render(request, 'login.html')

def mypage(request):
    return render(request, 'mypage.html')


class CustomLoginView(auth_view.LoginView):
    form_class = CustomAuthenticationForm

