from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'phone_number', 'favorite_genre', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'phone_number': {'required': False},
            'favorite_genre': {'required': False},
        }

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number', ''),
            favorite_genre=validated_data.get('favorite_genre', ''),
            password=validated_data['password'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
