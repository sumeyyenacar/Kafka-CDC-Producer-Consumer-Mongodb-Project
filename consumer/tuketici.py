import json  # JSON modülünü içe aktar

from kafka import KafkaConsumer  # kafka kütüphanesinden KafkaConsumer sınıfını içe aktar

kafka_bootstrap_servers = 'localhost:9092'  # Kafka başlangıç sunucularını belirle
kafka_topic = 'your_kafka_topic'  # Kafka konusunu belirle

consumer = KafkaConsumer(  # KafkaConsumer nesnesi oluştur
    kafka_topic,  # Abone olunacak konuyu belirt
    bootstrap_servers=kafka_bootstrap_servers,  # Kafka başlangıç sunucularını ayarla
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Değer çözümleyiciyi ayarla, JSON verilerini çözümlemek için
)

def consume_messages():
    for message in consumer:  # Her bir mesaj için döngüye gir
        print(message.value)  # Mesajın değerini ekrana yazdır

if __name__ == '__main__':
    consume_messages()  # Mesajları tüketmek için consume_messages fonksiyonunu çağır

