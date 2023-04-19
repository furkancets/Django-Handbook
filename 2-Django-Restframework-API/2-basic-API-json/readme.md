Hedef = Basit bir json döndüren API uygulaması.

* models.py

Her zaman ki gibi hiç şaşmadan bu bölümde veriyi tutmak istediğimiz şekli models.py'da açıklıyoruz.

Bunu bölümü SQL bilenler için şu şekilde açıklayabilirim CREATE TABLE... Aslında model'de oluşturduğumuz classlar SQLite, MySQL veya PostgreSQL'de kullandığımız kolon isimlerini oluştururlar.

* views.py 

Bir önceki çalışmada kullandığımız generic fonksiyonları yerine eğer method POST ise veya GET ise diye tanımlayarak fonksiyonların içinde bir logic kuruyoruz.

Fonksiyon çıktılarını json nesnelerine eşitliyoruz.

* urls.py

Bu sefer urls.py standart view'u aldığımızı göreceksinz. Herhangi bir as_view gibi methodlar kullanmadan.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t basicapijson:0.0.1 .

docker run -p 8000:8000 -d --name jsoncontainer basicapijson:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

docker exec -it jsoncontainer /bin/bash

http://127.0.0.1:8000/api/books linkine ulaştıktan sonra methodları deneyebilirsiniz.

Not: Çalıştırdıktan sonra illa superuser oluşturmak zorunda değilsiniz ama admin tarafında bunlarında nasıl değişiklik gösterdiğini gözlemlemek adına güzel bir tecrübe olabilir.

* python manage.py createsuperuser

Not : Python 3.10.8 versiyonu kullanılmıştır.