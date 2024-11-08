import os
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import matplotlib.pyplot as plt
load_dotenv()  # Carga las variables desde .env

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
#4
sp = spotipy.Spotify(auth_manager=SpotifyOAuth)
#5
artista_id = '2Eo4Yaukt9d6dnZrY5hQKi'
# Obtener las canciones principales
top_tracks = sp.artist_top_tracks(artista_id, country='ar')['tracks'][:10]

# Extraer el nombre de la canción, popularidad y duración
for track in top_tracks:
    name = track['name']
    popularity = track['popularity']
    duration_min = track['duration_ms'] / 60000
    print(f"'{name}' - Popularidad: {popularity}, Duración: {duration_min:.2f} minutos")

#6
# Crear lista de diccionarios para cada canción
tracks_data = [ {'Nombre': track['name'], 
     'Popularidad': track['popularity'], 
     'Duración_min': track['duration_ms'] / 60000} 
    for track in top_tracks]
    # Crear DataFrame
df_tracks = pd.DataFrame(tracks_data)

# Ordenar por popularidad de forma creciente y mostrar top 3
df_tracks_sorted = df_tracks.sort_values(by='Popularidad').head(3)
print(df_tracks_sorted)

# Crear el scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_tracks['Duración_min'], df_tracks['Popularidad'], color='red')
plt.title("Relación entre la duración de la canción y su popularidad")