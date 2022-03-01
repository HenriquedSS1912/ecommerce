from django.urls import path
from . import views

app_name = 'sobre'

urlpatterns = [
    path('projeto/', views.Projeto.as_view(), name="projeto"),
    path('desenvolvedor/', views.Desenvolvedor.as_view(), name="desenvolvedor"),
]