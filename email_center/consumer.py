
import json
import pika
import django
import os

from django.core.mail import send_mail


# Your path to settings.py file
# path.append('C:/gostack/rabbitmq-example/likes/settings.py')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_center.settings')
django.setup()
from core.models import Email

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='tickets', durable=True)


def callback(ch, method, properties, body):
    print("Received in tickets...")
    data = json.loads(body)

    if properties.content_type == 'ticket_created':       
        user_email = data['user']['email'] 
        subject = f"Ticket comprado por {data['user']['username']} - {data['user']['email']}"
        data = f"Olá, seu ticket par o jogo {data['game']['name']} já está disponível. Segue código de acesso: {data['uuid']} / Setor: {data['sector']} / Lugar: {data['place']}."
        quote = Email.objects.create(subject=subject, body=data)
        quote.save()

        send_mail(
            subject,
            data,
            'ticketsnow@teste.com',
            [user_email],
            fail_silently=False,
        )


channel.basic_consume(
    queue='tickets', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
