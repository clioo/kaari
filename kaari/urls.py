from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.pages.urls')),
    path('listings/', include('apps.listings.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('realtors/', include('apps.realtors.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
