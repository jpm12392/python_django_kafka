# python_django_kafka

🚀 Django Microservices Project (Kafka-based)
📌 Project Overview

This project demonstrates a Django-based microservices architecture using Apache Kafka for asynchronous communication between services. The system is designed to be scalable, fault-tolerant, and event-driven, following real-world backend architecture patterns.

The entire project is open-source and deployed on GitHub for free to help developers understand microservices implementation with Django.

🧩 Architecture Highlights

Microservices-based backend using Django

Apache Kafka for inter-service communication

Event-driven architecture

Saga pattern for distributed transaction handling

Outbox pattern to ensure reliable event publishing

Idempotent consumers to handle duplicate events

Independent databases per service


🛠️ Tech Stack

Backend: Django, Django REST Framework

Messaging: Apache Kafka

Database: SQLite 

Containerization: Docker & Docker Compose

Version Control: Git & GitHub

🔐 Key Features

Loosely coupled services

Reliable message delivery

Fault-tolerant design

Scalable microservice communication

Clean and maintainable codebase

📂 Repository

🔗 GitHub: [\[Add your repository link here\]](https://github.com/jpm12392/python_django_kafka)

Deployed and maintained completely free on GitHub


🎯 Use Cases

Learning microservices with Django

Kafka-based event-driven systems

Backend architecture reference project

Interview-ready system design example

👨‍💻 Author Note

This project is built to demonstrate real-world microservices patterns using Django and Kafka. Contributions, issues, and suggestions are welcome!

When you use Kafka with Django microservices, you cannot do a traditional DB rollback across services. Kafka is event-driven and eventually consistent, so rollback is handled using design patterns, not transaction.rollback().

❌ What You CANNOT Do

No distributed DB rollback across services

No ACID transaction across Kafka + multiple microservices

No rollback() once a message is published to Kafka

Concept

Instead of rollback, you perform compensating actions.