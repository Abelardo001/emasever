from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import enviar_email   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  
    path('enviar-email/', enviar_email, name='enviar_email'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
