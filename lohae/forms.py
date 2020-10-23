from django import forms
from .models import Message



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