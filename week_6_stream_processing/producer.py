from time import sleep
from json import dumps
from kafka import KafkaProducer
import uuid


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    uid = uuid.uuid4()
    data = {'number': str(e) + str(uid)}
    producer.send('demo_1', value=data)
    print("producing" + " " + str(e) + str(uid))
    sleep(1)
