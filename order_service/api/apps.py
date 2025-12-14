from django.apps import AppConfig
import os

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        # Prevent running in autoreloader parent process
        if os.environ.get('RUN_MAIN') != 'true':
            return

        print("Order Service: Starting Kafka consumer...")
        from api.consumer import run_consumer_thread
        run_consumer_thread()
