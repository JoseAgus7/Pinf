from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # El campo nickname ahora es obligatorio y debe ser único
    nickname = models.CharField(max_length=255, unique=True)

    # Hacer el campo email obligatorio y único
    email = models.EmailField(unique=True)

    # Campo adicional por si lo requieres
    favorite_genre = models.CharField(max_length=50, blank=True)

    # Los campos de contraseña son manejados automáticamente por AbstractUser

    # Método para promover un usuario a superusuario
    def make_superuser(self):
        self.is_superuser = True
        self.is_staff = True
        self.save()

    # Método para revocar el estatus de superusuario
    def revoke_superuser(self):
        self.is_superuser = False
        self.is_staff = False
        self.save()

    # Sobrescribe el método save para hacer alguna lógica adicional si es necesario
    def save(self, *args, **kwargs):
        # Aquí podrías incluir cualquier lógica adicional que desees ejecutar cuando se guarda el usuario.
        super().save(*args, **kwargs)
    
    
