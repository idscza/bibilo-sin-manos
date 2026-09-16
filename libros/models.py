from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

# Create your models here.
