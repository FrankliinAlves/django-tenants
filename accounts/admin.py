from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# No tenant, usamos o UserAdmin padrão do Django ou um ModelAdmin simples
@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Permissões CRM', {'fields': ('as_permission', 'telefone')}),
    )
    list_display = ('username', 'email', 'as_permission', 'is_staff')
    