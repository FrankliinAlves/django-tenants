from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_tenants.utils import schema_context
from django.contrib.auth import get_user_model
from .models import Client


User = get_user_model()

@receiver(post_save, sender=Client)
def create_tenant_master_user(sender, instance, created, **kwargs):
    if not created or instance.schema_name == 'public':
        return

    def create_user():
        with schema_context(instance.schema_name):
            if not User.objects.filter(username=f'admin_{instance.schema_name}').exists():
                User.objects.create_superuser(
                    username=f'admin-{instance.schema_name}',
                    email=f'admin@{instance.schema_name}.com.br',
                    password='senha102030',
                    as_permission='master',
                    is_staff=True,
                    is_superuser=True,
                )
                print(f"✅ Usuário Master criado no tenant {instance.schema_name}")

    transaction.on_commit(create_user)
