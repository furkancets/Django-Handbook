Hedef = Basit bir menu sistemi yapmak.

* models.py 

Öncelikle models.py'dan başlanmalı burada kayıt altına alıcanacak veriler uygun formatta tanıtılmalı.

* admin.py

Bu kısma yine models.py'da oluşturduğumuz Menu methodunu çağırırız.

admin.site.register(Menu) şeklinde ekleriz.

* views.py

Burada oluşturduğumuz "menu" fonksiyonunu, models'te tasarladığımız "Menu" class'ına query yollayarak kuruyoruz.

* menu.html

Bu sayede template'mizde rahatlıkla views'ta oluşturduğumuz "menu" fonksiyonumuzu kullanabiliyoruz.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli 

* docker build -t basicmenuitems:0.0.1 .  
* docker run -p 8000:8000 -d --name menucontainer basicmenuitems:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;
* docker exec -it menucontainer /bin/bash
* cd myproject
* python manage.py createsuperuser

Not : Python 3.10.8 versiyonu kullanılmıştır.