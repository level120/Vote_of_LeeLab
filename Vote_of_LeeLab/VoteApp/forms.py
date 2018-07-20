"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Like

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username or ID'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['name_id', 'name', 'description']
        widgets = {
            # 'name_id' : forms.TextInput(attrs={'class': 'form-control readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '후보자의 이름을 정해주세요.'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '투표 페이지에 나타낼 메세지를 입력하세요.'}),
        }
        labels = {
            'name_id': 'No',
            'name': '후보자 이름',
            'description': '후보자 소개'
        }

    def __init__(self, *args, **kwargs):
        super(LikeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['maxlength'] = 8
        self.fields['description'].widget.attrs['maxlength'] = 30


    def merge_from_initial(self):
        filt = lambda v: v not in self.data.keys()
        for field in filter(filt, getattr(self.Meta, 'fields', ())):
            self.data[field] = self.initial.get(field, None)

