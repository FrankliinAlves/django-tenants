from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Admin específico do Tenant (opcional, para o Master gerenciar usuários)
    path('admin/', admin.site.urls),

    # Rota raiz
    path('', views.home, name='home'),
    
    # Tela de login
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # Tela ao logar
    path('logged/', views.LoggedView.as_view(), name='logged'),
]
