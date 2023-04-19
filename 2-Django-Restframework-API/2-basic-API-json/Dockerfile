FROM python:3.10-slim-buster

WORKDIR /basicapijson

COPY  . /basicapijson

RUN pip3 install -r requirements.txt

RUN python manage.py makemigrations && python manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]