import threading
from kafka import KafkaConsumer
from api.models import UserOrderNotification
import json

def start_consumer():
    consumer = KafkaConsumer(
        'order_created',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )

    print("Notification Service consumer running...")

    for msg in consumer:
        notifications = UserOrderNotification()
        notifications.order_id = msg.value[0]['order_id']
        notifications.messages = msg.value[0]['messages']
        notifications.save()
        print("Notification received:", msg.value)

def run_consumer_thread():
    t = threading.Thread(target=start_consumer, daemon=True)
    t.start()
