# Generated by Django 2.2 on 2020-04-11 23:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200411_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de venta',
                'verbose_name_plural': 'Tipos de venta',
            },
        ),
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Baños'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(verbose_name='Recámaras'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0, verbose_name='Cochera'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='¿Sigue a la venta?'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha publicada'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Metros cuadrados'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Foto 1'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Foto 2'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Foto 3'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Foto 4'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Foto 5'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Foto 6'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Foto principal'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor', verbose_name='Agente'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(verbose_name='Metros cuadrados construidos'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(max_length=100, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=20, verbose_name='Código postal'),
        ),
        migrations.AddField(
            model_name='listing',
            name='sell_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='listings.SellType', verbose_name='Tipo de venta'),
            preserve_default=False,
        ),
    ]
