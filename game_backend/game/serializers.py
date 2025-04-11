from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'username', 'email', 'score', 'level', 'coins', 'avatar')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        player = Player.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return player

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        player = authenticate(**data)
        if player and player.is_active:
            return player
        raise serializers.ValidationError("Incorrect Credentials")