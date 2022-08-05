from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=100)
    amount_tickets_total = models.PositiveBigIntegerField()
    amount_tickets_available = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    uuid = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sector = models.CharField(max_length=10)
    place = models.CharField(max_length=10)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.uuid} - {self.user}'
