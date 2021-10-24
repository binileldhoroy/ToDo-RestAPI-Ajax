from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name='api-overview'),
    path('task-list/',views.taskView,name='task-view'),
    path('task-details/<str:pkey>',views.taskDetail,name='task-details'),
    path('task-create/',views.taskCreate,name='task-create'),
    path('task-update/<str:pkey>',views.taskUpdate,name='task-update'),
    path('task-delete/<str:pkey>',views.taskDelete,name='task-delete'),
]