FROM python:3.10-slim-buster

WORKDIR /basic-menu-items

COPY  . /basic-menu-items

RUN pip3 install -r requirements.txt

RUN python myproject/manage.py makemigrations && python myproject/manage.py migrate

CMD ["python3", "myproject/manage.py", "runserver", "0.0.0.0:8000"]