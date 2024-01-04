from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django import forms
from account.models import *

    
def start_with_0(value):
    if value[0] != 0:
        raise forms.ValidationError('Phone number should start with 0')


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), validators=[validators.MaxLengthValidator(15)])
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), validators=[validators.MaxLengthValidator(11), start_with_0])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password_1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('%(value)s is taken',
                                  code="taken",
                                  params={'value' : f'Username'}) 
        return username
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError('%(value)s is already signed up',
                                  code="signed_up",
                                  params={'value' : f'Phone'}) 
        return phone
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Passwords don't match")
        return password_confirm
    

class OtpForm(forms.Form):
    otp = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), validators=[validators.MaxLengthValidator(4)])
     
    
class CheckoutForm(forms.ModelForm):
    user = forms.IntegerField(required=False)
    class Meta:
        model = Address
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
