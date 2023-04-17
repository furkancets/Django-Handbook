Hedef = Basit bir restoran rezervasyon ve menu uygulaması.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t bookingmenu:0.0.1 .

docker run -p 8000:8000 -d --name restaurantcontainer bookingmenu:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

docker exec -it restaurantcontainer /bin/bash

cd myproject

* python manage.py createsuperuser

Not : Python 3.10.8 versiyonu kullanılmıştır.