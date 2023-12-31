from threading import Thread
from channels.layers import get_channel_layer
from faker import Faker
import random
from .models import Student
import json
fake = Faker()
from asgiref.sync import async_to_sync
import time


class CreateStudentThread(Thread):

    def __init__(self, total):
        self.total = total
        Thread.__init__(self)

    
    def run(self):
        try:
            print('thread excecution staeted')
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total +=1
                student_obj = Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10,50)
                )
                channel_layer = get_channel_layer()
                
                data =  {
                    'current_total': current_total ,
                    'total' : self.total,
                    'student_name': student_obj.student_name,
                    'student_email': student_obj.student_email,
                    'student_address': student_obj.address,
                    'student_age': str(student_obj.age)
                }
                
                # print(data)
                async_to_sync(channel_layer.group_send)(
                'student_group_name', {
                    'type': 'send_notification',
                    'value': json.dumps(data)
                }
            )
            # time.sleep(1)

        except Exception as e:
            print(e) 