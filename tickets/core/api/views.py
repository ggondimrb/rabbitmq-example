from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
import uuid

from core.models import Game, Ticket
from core.producer import publish
from .serializers import TicketSerializer, TicketModelSerializer


class TicketViewset(ViewSet):

    def list(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketModelSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        json_data = request.data
        serializer = TicketSerializer(data=json_data)
        serializer.is_valid(raise_exception=True)

        game = Game.objects.get(id=json_data['game'])
        if game.amount_tickets_available == 0:
            return Response('Não existem ingressos disponíveis', status=status.HTTP_400_BAD_REQUEST)

        already_exist_ticket = Ticket.objects.filter(
            sector=json_data['sector'], place=json_data['place'], game__id=json_data['game'])

        if already_exist_ticket:
            return Response({'error': 'O ingresso selecionado já foi vendido'}, status=status.HTTP_400_BAD_REQUEST)

        ticket_data = {
            "uuid": uuid.uuid4(),
            "user_id": json_data['user'],
            "sector": json_data['sector'],
            "place": json_data['place'],
            "game_id": json_data['game']
        }
        ticket_data = Ticket.objects.create(**ticket_data)

        game.amount_tickets_available -= 1
        game.save()
        serializer = TicketModelSerializer(ticket_data)
        publish('ticket_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
