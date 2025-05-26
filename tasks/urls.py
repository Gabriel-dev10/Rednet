from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova_task/', views.criar_task, name='criar_task'),
    path('deletar_task/<int:task_id>', views.deletar_task, name='deletar_task'),
    path('detalhar_task/<int:task_id>/', views.detalhar_task, name='detalhar_task'),
    path('atualizar_task/<int:task_id>/', views.atualizar_task, name='atualizar_task'),
    path('exportar_json/', views.exportar_latencia_json, name='exportar_latencia_json'),
]
