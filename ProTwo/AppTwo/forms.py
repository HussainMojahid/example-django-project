
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core import validators
from django import forms
from .models import UserProfileInfo

from .models import users

def check_x(value):
    if value[0] == 'x':
        raise forms.ValidationError("You may from china , chinese were not allowd")

class NewForm(forms.Form):
    fname = forms.CharField(max_length=100,label='First Name',validators=[check_x])
    lname = forms.CharField(max_length=100,label='Last Name',validators=[validators.MinLengthValidator(5)])
    email = forms.EmailField(max_length=100,label='Email')
    v_mail = forms.EmailField(max_length=70,label="enter again")
    botcatcher = forms.CharField(required=False,widget= forms.HiddenInput)


    def clean_botcatcher(self):
            botcatcher = self.cleaned_data['botcatcher']
            if len(botcatcher)>0:
                print("not valid user trying to enter")
                raise ValidationError('bot is not allowed')
            return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_mail = all_clean_data['v_mail']

        if email != v_mail:
            raise ValidationError("make sure both email same")

class DataCollectionForm(forms.ModelForm):
    class Meta:
        model = users
        fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site',"profile_pic")