from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_view
from .forms import CustomAuthenticationForm
from .forms import MsgForm
from .models import Message

# Create your views here.

def main(request):
    all_msg = Message.objects.all()
    return render(request, 'main.html', {'all_msg':all_msg})

def productlist(request):
    return render(request, 'productlist.html')

def buy_item(request):
    return render(request, 'buy_item.html')

def write_messages(request):
    if request.method == "POST":
        filled_form = MsgForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('main')
    msg_form = MsgForm()
    return render(request, 'write_messages.html', {'msg_form':msg_form})

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


