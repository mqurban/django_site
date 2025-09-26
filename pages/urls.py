from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('video-detail.html/', views.video_detail, name='video-detail.html'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path("photo-detail.html/", views.photo_detail, name="photo-detail.html"),  # only one
]
