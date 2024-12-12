from django.db import models

class Proyectos(models.Model):
    titulo = models.CharField(max_length=200)
    introduccion = models.CharField(max_length=250)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="Proyectos")
    video = models.FileField(upload_to="Proyectos", blank=True, null=True)
    link = models.URLField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion= models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-creacion"]


    def __str__(self):
        return self.titulo




class ImagenProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos, related_name="imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="Proyectos/Imagenes")

    def __str__(self):
        return f"Imagen de {self.proyecto.titulo}"


class VideoProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos, related_name="videos", on_delete=models.CASCADE)
    video = models.FileField(upload_to="Proyectos/Videos")

    def __str__(self):
        return f"Video de {self.proyecto.titulo}"
    
    
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    nacimiento = models.DateField()
    titulo = models.CharField(max_length=250)
    cv = models.FileField(upload_to="curriculums")
    sobre_mi = models.TextField()
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.titulo}"
    
    