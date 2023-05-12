from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)
    foto = models.ImageField(upload_to='fotos',null=True)

    def __str__(self) -> str:
        return super().__str__()
    
class Mascota(models.Model):
    idMascota=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45)
    raza=models.CharField(max_length=45)
    edad=models.IntegerField()
    descripcion=models.TextField()
    foto=models.ImageField(upload_to='fotos',null=True,default='fotos/default.jpg')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    publicado=models.BooleanField(default=False)
    comentario=models.TextField(null=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        return self.nombre

class Galeria(models.Model):
    idFoto =models.AutoField(primary_key=True)
    foto= models.ImageField(upload_to='galeria',null=True)
    mascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.idFoto)+" "+(self.mascota.nombre)