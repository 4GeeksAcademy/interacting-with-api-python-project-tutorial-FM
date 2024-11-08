import os
import pandas as pd
from dotenv import load_dotenv
import spotipy

load_dotenv()  # Carga las variables desde .env

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth)
artista_id = '2Eo4Yaukt9d6dnZrY5hQKi'

# Obtener las canciones principales
top_tracks = sp.artist_top_tracks(artista_id, country='ar')['tracks'][:10]

# Extraer el nombre de la canción, popularidad y duración
for track in top_tracks:
    name = track['name']
    popularity = track['popularity']
    duration_min = track['duration_ms'] / 60000
    print(f"'{name}' - Popularidad: {popularity}, Duración: {duration_min:.2f} minutos")