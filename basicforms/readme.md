Hedef = Basit bir rezervasyon sistemi yapmak.

* models.py 

Öncelikle models.py'dan başlanmalı burada kayıt altına alıcanacak veriler uygun formatta tanıtılmalı.

* admin.py

Bu kısma yine models.py'da oluşturduğumuz Booking methodunu çağırırız.

admin.site.register(Booking) şeklinde ekleriz.

* forms.py 

Daha sonra forms.py kısmı dosya olarak olurşturulur ve models.py'da oluşturduğunuz Booking methodunu buradan çağırırız. 

Meta class'ı django'nun default methodudur. Model olarak Booking'i kullanacağınızı söylemiş olursunuz. fields = "__all__" ile validaditon kısmı halledilir eğer herhangi bir input boş gönderilirse hayıt gerçekleşmez.


Uygulamayı çalıştırmak için dockerize etmeniz yeterli 

* docker build -t basicform:0.0.1 .  
* docker run -p 8000:8000 -d basicform:0.0.1 

Not : Python 3.10.8 versiyonu kullanılmıştır.
