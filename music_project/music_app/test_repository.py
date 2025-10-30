from music_app.models import Artist, Album, Genre
from music_app.repositories import UnitOfWork

# Створюємо об'єкт UnitOfWork
uow = UnitOfWork()

# -----------------------------
# 1. Додавання нового запису
# -----------------------------
# Новий артист
new_artist = Artist(nickname="JuiceWRLD", real_name="Jarad Higgins", birth_year=1998, country="USA")
uow.artists.add(new_artist)

# Новий жанр
new_genre = Genre(name="Hip-Hop", description="Hip-Hop Music")
uow.genres.add(new_genre)

# Новий альбом
new_album = Album(title="Legends Never Die", release_year=2020)
uow.albums.add(new_album)

# Додаємо артиста до альбому (ManyToMany)
new_album.artists.add(new_artist)

# -----------------------------
# 2. Виведення всіх записів
# -----------------------------
print("All Artists:")
for artist in uow.artists.get_all():
    print(f"{artist.id}: {artist.nickname}, {artist.real_name}, {artist.birth_year}, {artist.country}")

print("\nAll Genres:")
for genre in uow.genres.get_all():
    print(f"{genre.id}: {genre.name}, {genre.description}")

print("\nAll Albums:")
for album in uow.albums.get_all():
    print(f"{album.id}: {album.title}, {album.release_year}, Artists: {[a.nickname for a in album.artists.all()]}")

# -----------------------------
# 3. Пошук по ID
# -----------------------------
artist_by_id = uow.artists.get_by_id(new_artist.id)
print(f"\nArtist found by ID {new_artist.id}: {artist_by_id.nickname}, {artist_by_id.real_name}")
