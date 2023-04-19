Hedef = Basit bir kütüphane API uygulaması.

* models.py

Her zaman ki gibi hiç şaşmadan bu bölümde veriyi tutmak istediğimiz şekli models.py'da açıklıyoruz.

Bunu bölümü SQL bilenler için şu şekilde açıklayabilirim CREATE TABLE... Aslında model'de oluşturduğumuz classlar SQLite, MySQL veya PostgreSQL'de kullandığımız kolon isimlerini oluştururlar.

* views.py 

Bu bölümde her zaman olduğu gibi validasyon işlemşlerini gerçekleştireceğiz. PUT request ile gelen veriyi uygun formatta girişinin yapılıp yapılmadığını kontrol edeceğiz.

Burada generic gibi bazı özelleştirilmiş kütüphaneler yardımıyla veridem rahatlıkla render alacağız.

rest_framework'un içinde bulunan Generics gibi kütüphaneleri nasıl kullanılacaklarına dair bir notion yazısını buraya iliştireceğim.

* serializers.py

Yeni bir dosya bunu app düzeyinde manuel olarak ekleyerek kendimiz geliştiriyoruz. Bu noktada asıl validasyon gerçekleşiyor. API ile servis ettiğimiz verinin(GET) hangi bölümlerinin kullanıcıya görünüp görünmeyeceği gibi konularda kararlarımızı belirtiyoruz.

* urls.py

POST ederken oluşturduğumuz id'yi, spesific tek bir kayıta gidelecek id değişkeni url'e tanımlarız.

Bu işlem'in SQL sorgusunda where conditions yazmaktan bir farkı yoktur.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t basicapi:0.0.1 .

docker run -p 8000:8000 -d --name requestscontainer basicapi:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

docker exec -it requestscontainer /bin/bash

http://127.0.0.1:8000/api/books linkine ulaştıktan sonra methodları deneyebilirsiniz.

http://127.0.0.1:8000/api/books/1 size spesifik ID'deki elemanı getirecektir.

Not: Çalıştırdıktan sonra illa superuser oluşturmak zorunda değilsiniz ama admin tarafında bunlarında nasıl değişiklik gösterdiğini gözlemlemek adına güzel bir tecrübe olabilir.

* python manage.py createsuperuser

Not : Python 3.10.8 versiyonu kullanılmıştır.