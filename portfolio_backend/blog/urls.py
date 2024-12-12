from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.articulos, name='articulos'),
    path('articulo/<int:id>/', views.articulo, name='articulo'),
]