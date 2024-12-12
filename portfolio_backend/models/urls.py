from django.urls import path
from . import views


urlpatterns = [
    path('proyectos/', views.proyectos, name="proyectos"),
    path("proyecto/<int:id>/", views.proyecto, name="proyecto"),
    path("persona/<int:id>/", views.persona, name="persona")
]