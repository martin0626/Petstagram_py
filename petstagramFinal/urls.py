from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from petstagramFinal import settings

urlpatterns = [
    path('', include('petstagramFinal.common.urls')),
    path('pets/', include('petstagramFinal.pets.urls')),
    path('acoounts/', include('petstagramFinal.accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
