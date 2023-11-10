from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'favorite_genre', 'password', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'phone_number': {'required': False},
            'favorite_genre': {'required': False},
        }

    def validate_password(self, value: str) -> str:
        """
        Hash password on creation or update.
        """
        return make_password(value)

    def create(self, validated_data):
        # Se crea un nuevo usuario utilizando los datos validados
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number', ''),
            favorite_genre=validated_data.get('favorite_genre', ''),
            # Otros campos como 'first_name', 'last_name' se pueden agregar aquí si es necesario
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Actualiza el usuario existente utilizando los datos validados
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.favorite_genre = validated_data.get('favorite_genre', instance.favorite_genre)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number),
        instance.favorite_genre = validated_data.get('favorite_genre', instance.favorite_genre),
        # Otros campos como 'first_name', 'last_name' se pueden actualizar aquí si es necesario
        
        # Si la contraseña se incluye en los datos validados, se actualiza.
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance

