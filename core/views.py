from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model 
from .forms import CadastroForm, LoginForm
from django.contrib import messages

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
       
        login_data = request.POST.get('email') or ''
        password = request.POST.get('password') or ''
        
        username = login_data
        
        if "@" in login_data:
            try:
                user_obj = User.objects.get(email=login_data)
                username = user_obj.username
            except User.DoesNotExist:
                pass 

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('bemvindo')
        else:
            return render(request, 'core/login.html', {'error': "Usuário ou senha inválidos"})
    
    return render(request, 'core/login.html')

@login_required(login_url='login')
def BemVindo(request):
    return render(request, 'core/Boasvindas.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'core/home.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Sua conta foi excluída com sucesso.")
        return redirect('pagina_inicial') 