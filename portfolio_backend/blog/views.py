from django.shortcuts import get_object_or_404, render
from .models import Articulo
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings



def articulos(request):
    articulos = Articulo.objects.all()
    
    articulos_data = []
    for articulo in articulos:
        articulo_dict = model_to_dict(articulo)
        
       
        articulo_dict["imagen"] = articulo.imagen.url if articulo.imagen and hasattr(articulo.imagen, 'url') else None
        
        
        articulos_data.append(articulo_dict)

    return JsonResponse(articulos_data, safe=False)




def articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    

    data = {
        "titulo": articulo.titulo,
        "descripcion": articulo.descripcion,
        "imagen_principal": settings.MEDIA_URL + str(articulo.imagen) if articulo.imagen else None,
        "creacion": articulo.creacion,
        "modificacion": articulo.modificacion
    }

    return JsonResponse(data)