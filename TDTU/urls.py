from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from tdtu_app.views import home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
