from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission,User

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
     
    FAVORITE_GENERE_CHOICES = [
        ('terror', 'Terror'),
        ('comedia', 'Comedia'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('aventura', 'Aventura'),
        ('documentales', 'Documentales'),
        ('musicales', 'Musicales'),
        ('romance', 'Romance'),
        ('otros', 'Otros'),
    ]
    
    favorite_genre = models.CharField(
        max_length=50, 
        blank=True, 
        choices=FAVORITE_GENERE_CHOICES  
    )

    # Sobrescribe los campos heredados para resolver el conflicto de related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="custom_user_groups",
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name="custom_user_permissions",
        help_text='Specific permissions for this user.'
    )
    
    def make_superuser(self):
        self.is_superuser = True
        self.is_staff = True
        self.save()

    def revoke_superuser(self):
        self.is_superuser = False
        self.is_staff = False
        self.save()


class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')  #Falfaria el post assignarselo a la clase que tiene el video
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text