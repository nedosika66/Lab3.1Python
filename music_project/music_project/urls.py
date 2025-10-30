from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artists_view, name='artists'),
    path('songs/', views.songs_view, name='songs'),
]
