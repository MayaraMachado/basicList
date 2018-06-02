from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inserir', views.inserir, name="inserir_prod"),
    path('update/<int:id>', views.editar, name="edit_prod"),
    path('delete/<int:id>', views.delete, name="excluir_prod"),
]