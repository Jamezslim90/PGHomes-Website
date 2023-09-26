"""PGHomes_website URL Configuration

"""
from django.conf import settings # new
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estates/', include('estates.urls')),
    path('', include('pages.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
