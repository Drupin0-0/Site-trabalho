from django import forms
from .models import Usuario

class CadastroForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }
        error_messages = {
            'username': {
                'required': "Por favor, digite seu nome de usuário",
                'max_length': "O nome de usuário é muito longo",
                'invalid': "Use apenas letras, números e @/./+/-/_"
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem!")

        return cleaned_data
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Seu email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu email',
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        label="Sua Senha",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'autocomplete': 'current-password'
        })
    )
   