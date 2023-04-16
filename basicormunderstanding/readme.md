Hedef = Basit bir ORM sistemi anlamak.

* models.py
Öncelikle models.py'dan başlanmalı burada kayıt altına alıcanacak veriler uygun formatta tanıtılmalı.

* Bu bölümde herhangi bir views.py, .html, veya url ayarlamadan devam ediyoruz. Bundan dolayı Django'yu ayağı kaldırdığınızda karşınıza çıkan default görüntü gelecektir.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t basicormunderstanding:0.0.1 .

docker run -p 8000:8000 -d --name ormcontainer basicormunderstanding:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

docker exec -it ormcontainer /bin/bash

cd myproject

* python manage.py createsuperuser

* python manage.py shell 

Komutundan sonra aşağıdaki komutlaı çalıştırdığınızda başarı ile sqlite'a hayıt olduğunu göreceksiniz.
admin panelden kontol etmeniz iyi olur.

from myapp.models import DrinksCategory

cat = DrinksCategory(category_name='Alcohol')

cat.save()

Not : Python 3.10.8 versiyonu kullanılmıştır.
