from django.urls import path

from apps.listings import views

#Coming from apps.listings/ url

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]