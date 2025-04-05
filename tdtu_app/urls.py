from django.urls import path
from .views import home_views, news_views, reception_online, student_views, new_details, information_views

urlpatterns = [
    path('', home_views, name='home'),
    path('news', news_views, name='news'),
    path('reception-online', reception_online, name='reception-online'),
    path('student', student_views, name='students'),
    path('news/1', new_details, name='news_detail'),
    path('information-tdtu', information_views, name='information-tdtu' ),
]
