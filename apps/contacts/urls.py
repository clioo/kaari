from django.urls import path

from apps.contacts import views

urlpatterns = [
    path('contact', views.contact, name='contact')
]