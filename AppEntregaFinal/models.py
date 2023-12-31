from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Blogs(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descripcion = RichTextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="blogimagen", null=True, blank=True)
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.fecha}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"