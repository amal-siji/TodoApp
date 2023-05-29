
from datetime import timezone
from django import forms
from .models import Todo
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    task = forms.CharField()

    class Meta:
        model = Todo       
        fields = '__all__'
        exclude = ('user',)
        
    


class todoregisterform(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=255)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]


class loginform(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        

class taskeditform(forms.ModelForm):
    task = forms.CharField(max_length=255)

    class Meta:
        model = Todo
        
        fields ='__all__'
        exclude = ('user',)

