FROM python:3.10

WORKDIR /app

COPY	. .

RUN pip install -r requirements.txt

EXPOSE 8001


CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000