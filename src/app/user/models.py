from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Extensão do modelo User padrão do Django.
    
    Garante que cada usuário tenha um email único e adiciona funcionalidades extras.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def save(self, *args, **kwargs):
        """
        Valida e garante que o email seja único antes de salvar.
        """
        if User.objects.filter(email=self.user.email).exclude(pk=self.user.pk).exists():
            raise ValueError("Este email já está registrado.")
        super().save(*args, **kwargs)