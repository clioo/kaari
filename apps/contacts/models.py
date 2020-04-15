from django.db import models
from apps.listings.models import Listing,SellType


class Interest(models.Model):
    address = models.CharField(max_length=200, verbose_name='Dirección',
                                blank=True,null=True)
    city = models.CharField(max_length=100, verbose_name='Ciudad',
                                blank=True,null=True)
    state = models.CharField(max_length=100, verbose_name='Estado',
                                blank=True,null=True)
    zipcode = models.CharField(max_length=20, verbose_name='Código postal',
                                blank=True,null=True)
    price_from = models.IntegerField(verbose_name='Precio desde',
                                blank=True,null=True)
    price_to = models.IntegerField(verbose_name='Precio hasta',
                                blank=True,null=True)

    bedrooms = models.IntegerField(verbose_name='Recámaras',
                                blank=True,null=True)
    bathrooms = models.DecimalField(max_digits=2, 
                                decimal_places=1, verbose_name='Baños',
                                blank=True,null=True)
    garage = models.IntegerField(default=0, verbose_name='Cochera',
                                blank=True,null=True)
    is_interested = models.BooleanField(default=True, 
                                verbose_name='¿Sigue interesado?',
                                blank=True,null=True)
    sell_type = models.ForeignKey(SellType,on_delete=models.PROTECT,
                                verbose_name='Tipo de venta interesado',
                                blank=True,null=True)
    def __str__(self):
        return self.id
    class Meta:
        verbose_name = 'Interés del prospecto'
        verbose_name = 'Intereses del prospecto'

class OurListingInterest(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.PROTECT,
                                verbose_name="Inmueble interesado")
    message = models.TextField(blank=True,null=True)
    class Meta:
        verbose_name="Interés en nuestros inmuebles"
        verbose_name_plural="Intereses en nuestros inmuebles"
    

class Contact(models.Model):
    nss = models.CharField(max_length=100, 
                            verbose_name='Número de seguro social',
                            blank=True,null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, blank=True,
                            null=True)
    phone = models.CharField(max_length=100, unique=True)
    contact_date = models.DateTimeField(auto_now_add=True, blank=True,null=True,
                            verbose_name="Fecha de contacto")
    our_listing_interest = models.ManyToManyField(OurListingInterest,
                            verbose_name="Intereses en nuestro listado",
                                                blank=True,null=True)
    general_interests = models.ManyToManyField(Interest,
                            verbose_name='Intereses personales',
                            blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Contacto"
        verbose_name_plural="Contactos"