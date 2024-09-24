class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the total song count
        Song.count += 1
        
        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
            
        # Optionally, store genres and artists in a list or set
        if not hasattr(Song, 'genres'):
            Song.genres = set()
        Song.genres.add(genre)

        if not hasattr(Song, 'artists'):
            Song.artists = set()
        Song.artists.add(artist)
