from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import CadastroForm, LoginForm

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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user) # Cria a sessão do usuário
                return redirect('home') # Mande para a sua página inicial
            else:
                form.add_error(None, "Usuário ou senha inválidos")
    else:
        form = LoginForm()
    
    return render(request, 'core/login.html', {'form': form})