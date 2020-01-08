from django.urls import path, include
from . import views
 
urlpatterns = [
    path('', views.home, name="home"),

    path('<shorten_id>/', views.redirect_original_url, name='redirectoriginal'),
    # original_url 로 이동할 때
 
    path('home/makeshorturl/', views.shorten_url, name='shortenurl'),
    # shorten url을 만들 때
]