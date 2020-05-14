from django.urls import path

from apps.tasks.views import index, update_task, delete_task

urlpatterns = [

    path('', index, name='index'),
    path('update/<str:id>', update_task, name='update_task'),
    path('delete/<str:id>', delete_task, name='delete_task'),

]
