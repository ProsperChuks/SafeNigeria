from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]




if settings.DEBUG:
    # when in development, use static_url as route to render
    # static files (user-uploaded files)
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT
    )

    # when in development, use media_url as route to render
    # media files (user-uploaded files)
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )