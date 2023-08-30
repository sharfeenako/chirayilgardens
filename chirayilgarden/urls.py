from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('web.urls', namespace="web")),
    path('tinymce/', include('tinymce.urls')),
    path('translate/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False,
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
