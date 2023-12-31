from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class MyConsumers(WebsocketConsumer):


    def connect(self):
        self.room_name = 'test_consuner'
        self.room_group_name = 'test_consumer_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
            )

        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from django channels'}))


    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status': 'we got you'}))

    

    def disconnect(self, *args, **kwargs):
        print('disconnected')

    
    def send_notification(self, event):
        print('send_notification')
        print(event)
        data = json.loads(event.get('value'))
        # daata = json.dumps(data)

        self.send(text_data=json.dumps({"Payload" : data }))
        print('send_notification')


class NewConsumer(AsyncJsonWebsocketConsumer):


    async def connect(self):
        self.room_name = 'new_room'
        self.room_group_name = 'new_room_group'

        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({'status': 'connected from django channels'}))
    
    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status':"we got you"}))

    
    async def disconnect(self, *args, **kwargs):
        await print('disconnected')

    
    async def send_notification(self, event):
        print('send_notification')
        print(event)
        data = json.loads(event.get('value'))
        # daata = json.dumps(data)

        await self.send(text_data=json.dumps({"Payload" : data }))
        print('send_notification')



class Student_Thread(AsyncJsonWebsocketConsumer):


    async def connect(self):
        self.room_name = 'new_room'
        self.room_group_name = 'student_group_name'

        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({'status': 'connected from django channels'}))
    
    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status':"we got you"}))

    
    async def disconnect(self, *args, **kwargs):
        print('disconnected')

    
    async def send_notification(self, event):
        print(event)
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload': data}))