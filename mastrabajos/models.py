from django.db import models

# Create your models here.
class Empleos(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    paga = models.FloatField(blank=False,null=True)
    jornadas = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(blank=True,null=True, upload_to='Empresas')
    fecha_creacion = models.DateTimeField(blank=False, null=False) 
    email = models.EmailField()
    total_empleos = models.BooleanField(default=True)
    empleos = models.IntegerField(null=False, default=100)
    #video = models.FileField(upload_to='video')
    #enlace = models.URLField()

    def __str__(self):
         return self.nombre
    class Meta:
        verbose_name = ("Empleos")
        verbose_name_plural = ("Empleos disponibles")
     
class Empresas (models.Model):
    Marca = models.CharField(max_length=100, blank=False, null=True)
    #nombre = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    #paga = models.FloatField(blank=False,null=True)
    jornadas = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(null=True, upload_to='Empresas')
    #fecha_creacion = models.DateField(blank=False, null=False) 
    email = models.EmailField()
    #total_empleos = models.BooleanField(default=True)
    #empleos = models.IntegerField(null=False, default=100)
    video = models.FileField(upload_to='video')
    enlace = models.URLField()
    
    def __str__(self):
         return self.Marca
    class Meta:
        verbose_name = ("Empresas")
        verbose_name_plural = ("Empresas Disponibles")
    
class perfiles (models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    Especialidad = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.TextField(blank=False, null=False)
    telefono = models.FloatField(blank=False,null=True)
    #jornadas = models.CharField(max_length=100, blank=False, null=False)
    #image = models.ImageField(null=True, upload_to='Empresas')
    #fecha_creacion = models.DateField(blank=False, null=False) 
    email = models.EmailField()
    #total_empleos = models.BooleanField(default=True)
    #empleos = models.IntegerField(null=False, default=100)
    #video = models.FileField(upload_to='video')
    enlace = models.URLField()
    
    def __str__(self):
         return self.nombre
    class Meta:
        verbose_name = ("perfiles")
        verbose_name_plural = ("Usuarios")
        
#para poner formularios dependiendo de la pagina ( buscar tu propio formulario)
class comentarios ( models.Model): 
    nombre = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    telefono = models.FloatField(blank=False,null=True)
    Mensaje = models.CharField(max_length=100, blank=False, null=False)
        
    def __str__(self):
        return self.nombre
    
   