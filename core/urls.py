from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('Boasvindas/', views.BemVindo, name='bemvindo'),
    path('', views.home_view, name='pagina_inicial'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.delete_account, name='delete_account')
]