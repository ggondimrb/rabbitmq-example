
import json
import pika
import django
import os


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
        subject = f"Ticket comprado por {data['user']}"
        data = f"Olá, seu ticket par o jogo {data['game']['name']} já está disponível. Segue código de acesso: {data['uuid']} / Setor: {data['sector']} / Lugar: {data['place']}."
        quote = Email.objects.create(subject=subject, body=data)
        quote.save()
        print("email sended")


channel.basic_consume(
    queue='tickets', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
