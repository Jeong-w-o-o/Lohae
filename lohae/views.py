

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import views as auth_view
from .forms import CustomAuthenticationForm
from .forms import MsgForm, EditUserProfileForm
from .models import Message


# Create your views here.

def main(request):
    all_msg = Message.objects.all()
    return render(request, 'main.html', {'all_msg':all_msg})

def productlist(request):
    return render(request, 'productlist.html')

def buy_item(request):
    return render(request, 'buy_item.html')

def buy_item2(request):
    return render(request, 'buy_item2.html')   

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


def change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
        else:
            fm=EditUserProfileForm(instance=request.user)
        return render(request, 'change.html', {'name':request.user, 'form':fm})
    else:
        return redirect('change')

#비밀번호 바꾸기
def user_change_pass(request):
    if request.method == "POST":
         fm = PasswordChangeForm(user=request.user, data=request.POST)
         if fm.is_valid():
            fm.save()
            return redirect('main')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request, 'changepass.html', {'form':fm})
  