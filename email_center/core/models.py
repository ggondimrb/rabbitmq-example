from django.db import models


class Email(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.subject