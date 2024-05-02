from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_blog import views

# from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # In production, static files should be served by Whitenoise or a dedicated web server
    # Media files should be served by the web server directly
    pass
