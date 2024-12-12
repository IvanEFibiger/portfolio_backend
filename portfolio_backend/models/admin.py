from django.contrib import admin
from .models import Proyectos, ImagenProyecto, VideoProyecto, Persona

# Inline para imágenes
class ImagenProyectoInline(admin.TabularInline):  
    model = ImagenProyecto
    extra = 1  

# Inline para videos
class VideoProyectoInline(admin.TabularInline):
    model = VideoProyecto
    extra = 1  


@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    inlines = [ImagenProyectoInline, VideoProyectoInline]
    list_display = ('titulo', 'creacion', 'modificacion')
    search_fields = ('titulo', 'descripcion')
    
admin.site.register(Persona)