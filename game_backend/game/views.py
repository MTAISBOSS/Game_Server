from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import PlayerSerializer, RegisterSerializer, LoginSerializer
from .models import Player

class PlayerDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlayerSerializer
    
    def get_object(self):
        return self.request.user

class RegisterView(generics.CreateAPIView):
    queryset = Player.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        player = serializer.save()
        token = Token.objects.create(user=player)
        return Response({
            'player': PlayerSerializer(player, context=self.get_serializer_context()).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        player = serializer.validated_data
        token, created = Token.objects.get_or_create(user=player)
        return Response({
            'player': PlayerSerializer(player, context=self.get_serializer_context()).data,
            'token': token.key
        })

class UpdatePlayerView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get_object(self):
        return self.request.user