## 💻 Project

Example to use rabbitmq to connection between two django applications

## :rocket: Technologies

- [Django][django]
- [Django-rest-framework][django-rest-framework]
- [Rabbitmq][rabbitmq]
- [Docker][docker]

## :information_source: How To Use

To clone and run this application, you need [Git](https://git-scm.com), [Python][python] + [Docker][docker] installed on your computer.

### Instalação

```bash
# Clone this repository
$ git clone https://github.com/ggondimrb/rabbitmq-example

# Go into the project repository
$ cd rabbitmq-example
# run docker-compose:
$ docker-compose up

# Go into the ticket repository
$ cd ticket
# Activate the venv
$ cd venv/Scripts
$ /.Activate
# Go back to ticket repository
$ py manage.py runserver
# running on port 8000

# Go into the email_center repository
$ cd email_center
# Activate the venv
$ cd venv/Scripts
$ /.Activate
# Go back to email_center repository
$ py manage.py runserver 1234
# running on port 1234
# run the consumer
$ py consumer.py
```

[django]: https://www.djangoproject.com/
[django-rest-framework]: https://www.django-rest-framework.org/
[rabbitmq]: https://www.rabbitmq.com/
[docker]: https://www.docker.com/
[python]: https://www.python.org/
