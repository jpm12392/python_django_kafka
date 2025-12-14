import threading
from kafka import KafkaConsumer, KafkaProducer
from api.models import Order
import json

def start_consumer():
    consumer = KafkaConsumer(
        'user_created',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )

    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )

    print("Order Service consumer running...")

    for msg in consumer:
        orders = Order()
        orders.user_id = msg.value[0]['user_id']
        orders.order_name = msg.value[0]['order_name']
        orders.total_amount = msg.value[0]['total_amount']
        orders.save()

        event_data = [
            {
                "order_id":orders.id,
                'messages':"Your order has been received successfully."
            }
        ]
        producer.send("order_created", event_data)

def run_consumer_thread():
    t = threading.Thread(target=start_consumer, daemon=True)
    t.start()
