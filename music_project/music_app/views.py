from django.shortcuts import render
from .repositories import UnitOfWork

uow = UnitOfWork()

def artists_view(request):
    artists = uow.artists.get_all()
    return render(request, "music_app/artists.html", {"artists": artists})

def songs_view(request):
    songs = uow.songs.get_all()
    return render(request, "music_app/songs.html", {"songs": songs})
