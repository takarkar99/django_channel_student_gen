from django.urls import path
from Home.consumers import MyConsumers, NewConsumer, Student_Thread

ws_patterns = [
    path('ws/test/', MyConsumers.as_asgi()),
    path('ws/new/', NewConsumer.as_asgi()),
    path('ws/student/', Student_Thread.as_asgi()),
]