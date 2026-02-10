from django.contrib import admin
from .models import Client, Domain
from django_tenants.admin import TenantAdminMixin


class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1
    can_delete = False

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    # Adicionamos 'get_domain' na lista
    list_display = ('name', 'get_domain', 'schema_name', 'created_at')
    search_fields = ('name', 'schema_name')
    inlines = [DomainInline]
    ordering = ['id']

    # Função para buscar o domínio e exibir na coluna
    def get_domain(self, obj):

        domain = obj.domains.filter(is_primary=True).first()
        return domain.domain if domain else "Sem domínio"
    
    # Define o título da coluna no Admin
    get_domain.short_description = 'Domain'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('schema_name',)
        return self.readonly_fields

@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    list_filter = ('is_primary',)
