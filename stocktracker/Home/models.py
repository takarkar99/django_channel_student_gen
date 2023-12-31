from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync



class Notifiacation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.CharField(max_length=250)
    is_seen = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        # print(channel_layer)
        notification_obj = Notifiacation.objects.filter(is_seen=False).count()
        data = {'count': notification_obj, 'current_notification': self.notification} 

        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
            )
        
        print('save data')
        super().save(*args,**kwargs)


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    address = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return self.student_name