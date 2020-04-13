from django.db import models
from datetime import datetime
from apps.realtors.models import Realtor

class SellType(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre')
    class Meta:
        verbose_name='Tipo de venta'
        verbose_name_plural='Tipos de venta'

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name='Agente') #Don't delete listings when this foreign key is deleted
    title = models.CharField(max_length=200, verbose_name='Título')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    state = models.CharField(max_length=100, verbose_name='Estado')
    zipcode = models.CharField(max_length=20, verbose_name='Código postal')
    description = models.TextField(blank=True, verbose_name='Descripción') #Optional description, no max length
    price = models.IntegerField(verbose_name='Precio')
    bedrooms = models.IntegerField(verbose_name='Recámaras')
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Baños')
    garage = models.IntegerField(default=0, verbose_name='Cochera')
    sqft = models.IntegerField(verbose_name='Metros cuadrados construidos')
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Metros cuadrados')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Foto principal') #Save inside media folder under date structure
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 1') #Optional extra photos
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 2')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 3')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 4')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 5')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 6')
    is_published = models.BooleanField(default=True, verbose_name='¿Sigue a la venta?')
    list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Fecha publicada')
    sell_type = models.ForeignKey(SellType,on_delete=models.PROTECT,verbose_name='Tipo de venta')
    def __str__(self): #Show title as the identifier
        return self.title
    class Meta:
        verbose_name='Inmueble'
        verbose_name_plural='Inmuebles'