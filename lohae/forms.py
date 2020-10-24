from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Message
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "비밀번호나 아이디가 올바르지 않습니다. 다시 확인해 주세요."
        ),
        'inactive': ("이 계정은 인증되지 않았습니다. 인증을 먼저 진행해 주세요."),
    }
    def __init__(self, request=None, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs) # 꼭 있어야 한다!
        self.fields['username'].label = '유저이름'
        self.fields['password'].label = '비밀번호'


class MsgForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('content',)

    # 모델폼 customize
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['content'].label = " "
        self.fields['content'].widget.attrs.update({
            'class': 'msg_content',
            'placeholder': 'To. xxx',
        })

class EditUserProfileForm(UserChangeForm):
    passward = None
    class Meta:
        model=get_user_model()
        fields = ['username', 'date_joined', 'last_login']

class EditUserProfileForm(UserChangeForm):
    passward = None
    class Meta:
        model=get_user_model()
        fields = ['username', 'date_joined', 'last_login']