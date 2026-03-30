from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_email(self):
        """
        Valida se o email é único no sistema.
        Levanta ValidationError se o email já existe.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Este email já está registrado. Use outro email ou faça login.",
                code='email_exists'
            )
        return email
    
    def clean_username(self):
        """
        Valida se o username é único no sistema.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Este username já está em uso. Escolha outro.",
                code='username_exists'
            )
        return username


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def clean_email(self):
        """
        Valida se o email é único, excluindo o usuário atual.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Este email já está registrado por outro usuário.",
                code='email_exists'
            )
        return email
    
    def clean_username(self):
        """
        Valida se o username é único, excluindo o usuário atual.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Este username já está em uso.",
                code='username_exists'
            )
        return username


class SecureLoginForm(AuthenticationForm):
    """
    Form de login seguro que não revela se o usuário existe ou não.
    Mostra mensagem genérica para qualquer erro de autenticação.
    """
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )
            if self.user_cache is None:
                # Mensagem genérica por segurança
                raise forms.ValidationError(
                    "Esse usuário ou senha estão incorretos.",
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data