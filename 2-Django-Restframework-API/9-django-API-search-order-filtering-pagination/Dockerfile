FROM python:3.10-slim-buster

WORKDIR /restful-sofp

COPY  . /restful-sofp

RUN pip3 install -r LittleLemon/requirements.txt

RUN python LittleLemon/manage.py makemigrations && python LittleLemon/manage.py migrate

CMD ["python3", "LittleLemon/manage.py", "runserver", "0.0.0.0:8000"]