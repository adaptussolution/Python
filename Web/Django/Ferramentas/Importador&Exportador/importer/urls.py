from django.urls import path
from . import views

app_name = 'importer'

urlpatterns = [
    path('', views.ImportarDadosView.as_view(), name='importar_arquivo'),
]