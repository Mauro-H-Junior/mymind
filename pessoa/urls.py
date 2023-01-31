from django.urls import path
from . import views

urlpatterns = [
    path('atendimento/', views.listar_monitoramento, name='atendimento')
]
