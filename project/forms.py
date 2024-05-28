from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome usuario...',
            }
        ),
        label="Nome de usuario"
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'passwordInput',
                'placeholder':'Sua senha...',
            }
        ),
        label="Digite uma senha"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'passwordInput',
                'placeholder':'Confirme sua senha...',
            }
        ),
        label="Confirmar senha"
    )

    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2'
        )