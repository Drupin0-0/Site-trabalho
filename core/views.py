from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model # Use isso em vez de importar User
from .forms import CadastroForm, LoginForm

User = get_user_model()

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'core/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_data = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            username = login_data
            if "@" in login_data:
                try:
                    # Agora ele busca no seu modelo core.Usuario corretamente
                    user_obj = User.objects.get(email=login_data)
                    username = user_obj.username
                except User.DoesNotExist:
                    pass 

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('bemvindo')
            else:
                form.add_error(None, "Usuário ou senha inválidos")
    else:
        form = LoginForm()
    
    return render(request, 'core/login.html', {'form': form})

@login_required
def BemVindo(request):
    return render(request, 'core/Boasvindas.html')


def home_view(request):
    return render(request, 'core/home.html')
