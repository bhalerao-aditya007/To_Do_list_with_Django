from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name = 'addTask'),
    path('mark_as_done/<int:pk>', views.mark_as_done, name = 'done'),
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name = 'undone'),
    path('edit_task<int:pk>', views.edit_task, name = 'edit'),
    path('delete_task<int:pk>', views.del_task, name = 'delete'),
]