from django.shortcuts import get_object_or_404, render
from .models import Persona, Proyectos
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings

def proyectos(request):
    proyectos = Proyectos.objects.all()
    
    proyectos_data = []
    for proyecto in proyectos:
        proyecto_dict = model_to_dict(proyecto, exclude=['imagen', 'video'])
        
       
        proyecto_dict["imagen_principal"] = proyecto.imagen.url if proyecto.imagen and hasattr(proyecto.imagen, 'url') else None
        proyecto_dict["video_url"] = proyecto.video.url if proyecto.video and hasattr(proyecto.video, 'url') else None
        
        proyectos_data.append(proyecto_dict)

    return JsonResponse(proyectos_data, safe=False)


def proyecto(request, id):
    proyecto = get_object_or_404(Proyectos, id=id)
    
    # Preparar lista de URLs de imágenes adicionales
    imagenes_adicionales = [img.imagen.url for img in proyecto.imagenes.all()]  
    videos_adicionales = [vid.video.url for vid in proyecto.videos.all()]  

    # Estructura del JSON
    data = {
        "titulo": proyecto.titulo,
        "descripcion": proyecto.descripcion,
        "imagen_principal": settings.MEDIA_URL + str(proyecto.imagen) if proyecto.imagen else None,
        "video_principal": proyecto.video.url if proyecto.video else None,
        "imagenes": imagenes_adicionales,
        "videos": videos_adicionales,
        "link": proyecto.link,
        "creacion": proyecto.creacion,
        "modificacion": proyecto.modificacion
    }

    return JsonResponse(data)

def persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    data = {
        "nombre" : persona.nombre,
        "apellido" : persona.apellido,
        "foto_perfil" :  settings.MEDIA_URL + str(persona.foto_perfil) if persona.foto_perfil else None,
        "email" : persona.email,
        "telefono" : persona.telefono,
        "nacimiento" : persona.nacimiento,
        "titulo" : persona.titulo,
        "cv" : persona.cv.url if persona.cv else None,
        "sobre_mi" : persona.sobre_mi
    }
    return JsonResponse(data)