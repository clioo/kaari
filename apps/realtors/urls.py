from django.urls import path
from apps.realtors import views
urlpatterns = [
    path('', views.realtors_view, name='realtors'),
    path('<str:nombre>', views.get_realtor_view,name='realtor')
]