Hedef = http://127.0.0.1:8000/api/books/ gittiğiniz'de sağ üst köşede DjDT simgesine bakıp bunu keşfetmek.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t djangodebugtoolbar:0.0.1 .

docker run -p 8000:8000 -d --name debugcontainer djangodebugtoolbar:0.0.1

Not : Python 3.10.8 versiyonu kullanılmıştır.

https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker
