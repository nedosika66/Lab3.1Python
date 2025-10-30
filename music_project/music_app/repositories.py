from .models import Artist, Album, Genre, Song, Producer, StreamingPlatform
from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.db.models import Q

class Repository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, id):
        try:
            return self.model.objects.get(pk=id)
        except ObjectDoesNotExist:
            return None

    def add(self, instance):
        instance.save()
        return instance

    def update(self, id, **kwargs):
        obj = self.get_by_id(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None

    def delete(self, id):
        obj = self.get_by_id(id)
        if obj:
            obj.delete()
            return True
        return False

    def get_by_field(self, field_name, value):
        try:
            return self.model.objects.get(**{field_name: value})
        except (ObjectDoesNotExist, FieldError):
            return None

    def filter_by(self, **kwargs):
        try:
            return self.model.objects.filter(**kwargs)
        except FieldError:
            return self.model.objects.none()

class ArtistRepository(Repository):
    def __init__(self):
        super().__init__(Artist)

    def get_songs(self, artist_id):
        artist = self.get_by_id(artist_id)
        if artist:
            return Song.objects.filter(main_artist=artist)
        return []

class AlbumRepository(Repository):
    def __init__(self):
        super().__init__(Album)

class SongRepository(Repository):
    def __init__(self):
        super().__init__(Song)

class GenreRepository(Repository):
    def __init__(self):
        super().__init__(Genre)

class ProducerRepository(Repository):
    def __init__(self):
        super().__init__(Producer)

class StreamingPlatformRepository(Repository):
    def __init__(self):
        super().__init__(StreamingPlatform)

class UnitOfWork:
    def __init__(self):
        self.artists = ArtistRepository()
        self.albums = AlbumRepository()
        self.songs = SongRepository()
        self.genres = GenreRepository()
        self.producers = ProducerRepository()
        self.platforms = StreamingPlatformRepository()
