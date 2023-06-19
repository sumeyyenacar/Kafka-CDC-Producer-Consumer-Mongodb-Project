import time  # Zaman modülünü içe aktar

import json  # JSON modülünü içe aktar

from pymongo import MongoClient  # pymongo kütüphanesinden MongoClient sınıfını içe aktar

from kafka import KafkaProducer  # kafka kütüphanesinden KafkaProducer sınıfını içe aktar


mongo_host = 'mongodb://localhost:27017'  # MongoDB adresini belirle
mongo_db = 'kafka-deneme'  # MongoDB veritabanını belirle
mongo_collection = 'sumeyye12'  # MongoDB koleksiyonunu belirle
kafka_bootstrap_servers = 'localhost:9092'  # Kafka başlangıç sunucularını belirle
kafka_topic = 'your_kafka_topic'  # Kafka konusunu belirle

producer = KafkaProducer(  # KafkaProducer nesnesi oluştur
    bootstrap_servers=kafka_bootstrap_servers,  # Kafka başlangıç sunucularını ayarla
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Değer seri hale getiriciyi ayarla
)


client = MongoClient(mongo_host)  # MongoClient nesnesi oluştur ve MongoDB adresini kullanarak bağlan
db = client[mongo_db]  # Veritabanını seç
collection = db[mongo_collection]  # Koleksiyonu seç


def process_new_documents():
    last_document_id = None  # Son belge kimliği başlangıçta boş olarak ayarlanır

    while True:  # Sonsuz döngü
        query = {}  # Sorgu nesnesini oluştur

        if last_document_id:
            query['_id'] = {'$gt': last_document_id}  # Son belge kimliğinden büyük olan belgeleri almak için sorguya ekle

        new_documents = collection.find(query)  # Yeni belgeleri sorgula

        for doc in new_documents:  # Yeni belgelerin üzerinde döngü
            message = {'document': doc}  # Gönderilecek mesajı oluştur

            producer.send(kafka_topic, value=message)  # Kafka konusuna mesajı gönder

            last_document_id = doc['_id']  # Son belge kimliğini güncelle

        time.sleep(10)  # 10 saniye bekle

if __name__ == '__main__':
    process_new_documents()  # Fonksiyonu çalıştır
