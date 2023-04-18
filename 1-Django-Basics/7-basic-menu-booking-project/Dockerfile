FROM python:3.10-slim-buster

WORKDIR /menubookingproject

COPY  . /menubookingproject

RUN pip3 install -r requirements.txt

RUN python littlelemon/manage.py makemigrations && python littlelemon/manage.py migrate

CMD ["python3", "littlelemon/manage.py", "runserver", "0.0.0.0:8000"]