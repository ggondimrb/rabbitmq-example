from rest_framework.serializers import ModelSerializer
from core.models import Game, Ticket
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


class TicketSerializer(Serializer):
    user = serializers.IntegerField()
    sector = serializers.CharField(max_length=10)
    place = serializers.CharField(max_length=10)
    game = serializers.IntegerField()


class TicketModelSerializer(ModelSerializer):
    game = GameSerializer()
    user = UserSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'
