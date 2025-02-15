from kafka import KafkaConsumer
from json import loads
from time import sleep

consumer = KafkaConsumer(
    'datatalkclub.yellow_taxi_ride.json',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='consumer.group.id.demo.1',
    value_deserializer=lambda x: loads(x.decode('utf-8')))


while(True):
    print("inside while")
    for message in consumer:
        message = message.value
        print(message)
    sleep(1)
