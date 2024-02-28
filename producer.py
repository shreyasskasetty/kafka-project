from kafka import KafkaProducer
from data import get_registered_user
from time import sleep

import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_partitioner(key_bytes, all_partition, available_partition):
    return 0

# producer  = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                           value_serializer=json_serializer,
#                           partitioner=get_partitioner)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                          value_serializer=json_serializer)
if __name__ == "__main__":
    while 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        sleep(4)