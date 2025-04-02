from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from tdtu_app.views import home_views, news_views, reception_online

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views, name='home'),
    path('news', news_views, name='news'),
    path('reception-online', reception_online, name='reception-online'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
