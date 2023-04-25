FROM python:3.10-slim-buster

WORKDIR /djoserauth

COPY  . /djoserauth

RUN pip3 install -r requirements.txt

RUN python LittleLemon/manage.py makemigrations && python LittleLemon/manage.py migrate

CMD ["python3", "LittleLemon/manage.py", "runserver", "0.0.0.0:8000"]