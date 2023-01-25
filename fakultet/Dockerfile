FROM python:3.10

WORKDIR /app

COPY	./fakultet .

RUN pip install -r requirements.txt

EXPOSE 8000


CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000