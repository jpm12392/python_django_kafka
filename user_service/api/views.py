from rest_framework.views import APIView
from rest_framework.response import Response
from kafka import KafkaProducer
from api.models import User
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class CreateUser(APIView):
    def post(self, request):
        users = User()
        users.name = request.data['name']
        users.email = request.data['email']
        users.phone = request.data['phone']
        users.address = request.data['address']
        users.save()
        print("User records inserted in database.")
        user_data = [
            {
                "user_id":users.id,
                'order_name':request.data['order_name'],
                'total_amount':request.data['total_amount']
            }
        ]
        producer.send('user_created', user_data)
        return Response({"status": "User event sent"}, 201)
