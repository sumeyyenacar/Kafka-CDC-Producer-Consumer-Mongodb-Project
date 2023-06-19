<!-- omit in toc -->
# Apache Kafka ile Basit CDC Uygulaması - Mongodb

## İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Kurulum ve Gereksinimler](#kurulum-ve-gereksinimler)
- [Çalıştırma](#çalıştırma)
- [Lisans](#lisans)


## Proje Hakkında

Python programlama dilini kullanarak MongoDB veritabanında bir collection’da
oluşan yeni dökümanları sorgulayıp Apache Kafka’ya herhangi bir X topic altına bir JSON
mesajını üreten (procuder) ve bu X topic’deki mesajları tüketen (consumer) uygulamalar geliştirilmiştir.

![](.images/mimari.png)


Bu uygulama, veritabanındaki değişiklikleri yakalayarak bunları Kafka mesaj kuyruğuna aktarır. Bu sayede, veritabanındaki güncellemeleri gerçek zamanlı olarak takip etmek ve bu verileri farklı sistemlere iletmek mümkün olur. Proje, Kafka'nın güçlü ve ölçeklenebilir mesajlaşma sistemi özelliklerini kullanarak veri entegrasyonu ve senkronizasyonunu kolaylaştırır.

## Kurulum ve Gereksinimler

Docker Desktop'in yerel makinenizde kurulu olduğundan emin olun.(https://www.docker.com/products/docker-desktop) adresini ziyaret edebilirsiniz.

Seçtiğiniz programlama dilinde, MongoDB veritabanına bağlanmanız gerekiyor. İlgili programlama dilinin MongoDB sürücüsünü kullanarak, MongoDB'ye bağlanabilir ve veritabanı işlemlerini gerçekleştirebilirsiniz. Bu, yeni dökümanları sorgulamak ve tespit etmek için kullanılacak.

Seçtiğiniz programlama dilinde, Apache Kafka'ya bağlanmanız gerekiyor. Apache Kafka'ya bağlanmak için ilgili programlama dilinin Kafka sürücüsünü kullanabilirsiniz. Bu sürücü aracılığıyla Kafka'ya bağlanarak, üretici (producer) ve tüketici (consumer) uygulamalarınızı geliştirebilirsiniz.

## Çalıştırma

Projeyi çalıştırmak için projeyi klonlayın. Ardından proje dosyasını bilgisayarınıza kaydedin.
Komut satırında projenizin kayıtlı oladuğu dizine gidin ve 
```sh
cd ApacheKafka-CDC-Produce-Consumer-Mongodb-Project
```
yazın. Ardından projeyi çalıştırmak için
```sh
docker compose up --build
```
![](.images/build.png)

Uygulamayı kapatmak isterseniz
```sh
docker compose down
```
## Lisans

 MIT License Copyright (c) 2023 Sümeyye Naçar.