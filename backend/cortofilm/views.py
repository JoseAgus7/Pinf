from .models import User
from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'  # Usamos 'pk' (primary key) para buscar el usuario

class MakeSuperuserView(APIView):
    permission_classes = [permissions.IsAdminUser]  # Asegúrate de que solo los admin puedan hacer este cambio

    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            user.make_superuser()
            return Response({'message': 'Se realizó correctamente. Usuario ahora es superusuario.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class RevokeSuperuserView(APIView):
    permission_classes = [permissions.IsAdminUser]  # Solo los admin pueden revocar el estatus de superusuario

    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            user.revoke_superuser()
            return Response({'message': 'Se realizó correctamente. Superusuario ha sido revocado.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)