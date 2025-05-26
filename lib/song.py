class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.increment_genre_count(self.genre)
        Song.increment_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, song_genre):
        if song_genre not in cls.genres:
            cls.genres.append(song_genre)

    @classmethod
    def add_to_artists(cls, song_artist):
        if song_artist not in cls.artists:
            cls.artists.append(song_artist)

    @classmethod
    def increment_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def increment_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
