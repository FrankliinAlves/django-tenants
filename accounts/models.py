from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    PERMISSAO_CHOICES = (
        ('development', 'Development (Desenvolvedor)'),
        ('master', 'Master (Dono da Empresa)'),
        ('employee', 'Employee (Funcionário/Vendedor)'),
        ('view', 'View (Apenas Visualização)'),
    )
    
    as_permission = models.CharField(
        max_length=20, 
        choices=PERMISSAO_CHOICES, 
        default='employee'
    )

    telefone = models.CharField(max_length=15, blank=True)

    def save(self, *args, **kwargs):
        if self.as_permission == 'master':
            self.is_staff = True
        super().save(*args, **kwargs)
