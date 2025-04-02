from django.urls import path
from .views import home_views, news_views, reception_online

urlpatterns = [
    path('', home_views, name='home'),
    path('news', news_views, name='news'),
    path('reception-online', reception_online, name='reception-online'),

]
