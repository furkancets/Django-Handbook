Hedef = Bir template sistemi yaratıp footer oluşturabilmek. Footer'ı oluştururken farklı html'lere miras(inherit) edebilecek .html dosyaları oluşturmak.

Not: Artık bir önceki admin, model, settings, views taraflarına tekrar tekrar değinmeyeceğim. Bu dosyalardaki değişiklikleri ve hareket alanlarını görmek için bir önceki dosyalara geri dönün.

* partials/_header.html

Bu dosyada footer'ımızı temsil edecek tüm .html'leri static olarak ekliyoruz.

* base.html

Burası bize footer'da dolaştığımız sürece bir while döngüsünün içinde hereket ediyormuşuz gibi davranacak. 

About, menu, book gibi sekmelerde dolaşırken base.html üzerinde taşınacak.

Siz çarpı ya basıp session'u kapatana kadar.

* /*.html

Diğer tüm html'ler yukarıda bahsettiğim while döngüsünün canlı birer parçasıdır.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t inheritancefooter:0.0.1 .

docker run -p 8000:8000 -d --name footercontainer inheritancefooter:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

docker exec -it footercontainer /bin/bash

cd myproject

* python manage.py createsuperuser

Not : Python 3.10.8 versiyonu kullanılmıştır.
