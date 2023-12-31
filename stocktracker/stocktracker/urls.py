from django.contrib import admin
from django.urls import path, include
from Home.views import home, home_new,  home_student, generate_student_data


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('a/', home),
    path('b/', home_new),
    path('student/', home_student),
    path('student_gen/', generate_student_data)
]
