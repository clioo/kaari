from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Foto')
    shortName = models.CharField(max_length=15,verbose_name='Abreviación del nombre', unique=True)
    description = models.TextField(blank=True, verbose_name='Descripción')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.CharField(max_length=50, verbose_name='Correo')
    is_mvp = models.BooleanField(default=False, verbose_name='¿Gerente?')
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=True, verbose_name='¿Está activo?')
    def __str__(self): #Show name as the identifying field
        return self.name
    class Meta:
        verbose_name='Agente'
        verbose_name_plural='Agentes'
    
        