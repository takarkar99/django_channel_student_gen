from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
import json
from django.http import HttpResponse, JsonResponse
from .thread import *

def home(request):
    
        
    temp = 'Home/Home.html'

    for i in range(1,11):
        channel_layer = get_channel_layer()
        data = {'count': i}
        async_to_sync(channel_layer.group_send)(
            "test_consumer_group", {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        time.sleep(1)
    return render(request, temp)


async def home_new(request):   

   

    for i in range(1,11):
        channel_layer = get_channel_layer()
        data = {'count': i}
        await(channel_layer.group_send)(
            "new_room_group" , {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        time.sleep(1)

    return HttpResponse("render succefully")
    


def home_student(request):
     
     temp = 'Home/Home.html'
     return render(request, temp)
 

def generate_student_data(request):
    total = request.GET.get('total')
    print('total number student',total)
    obj = CreateStudentThread(int(total))
    obj.start()
    return JsonResponse({'status': 200})
