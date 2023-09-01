"""

/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
 
"""

# Paso 1: Configurar tu aplicación en el Panel de Desarrolladores de Spotify
  # - Ve al Panel de Desarrolladores de Spotify: https://developer.spotify.com/dashboard/
  # - Inicia sesión con tu cuenta de Spotify o crea una nueva si no tienes una.
  # - Haz clic en "Crear una aplicación" y sigue las instrucciones para registrar tu aplicación.
  # - Una vez que hayas registrado la aplicación, obtendrás un Cliente ID y un Cliente Secreto. Guárdalos en un lugar seguro, ya que los necesitarás en tu código.

# Paso 2: Instalar la biblioteca spotipy
  # pip install spotipy

# Paso 3: Autenticación y autorización
   # Importa la biblioteca spotipy y configure las credenciales de tu aplicación.abs

import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = 'ef88e9a32a404785832d31c18e69a633'
SPOTIPY_CLIENT_SECRET = '02651a5f4ac94a89a8eaf12c265a078c'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # Cambia esto si es necesario
scope = 'user-library-read user-modify-playback-state' # Tipos de funcionalidades que podre realizar con la API

sp = spotipy.Spotify(
                      auth_manager=SpotifyOAuth(
                                               client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope
                                            )
                    )



# Realiza una búsqueda para obtener las 10 primeras canciones del "Top 10 Global"
results = sp.playlist_tracks('4pXpF6wSZP6EiQYc2ZXxdR', limit=10)  # '37i9dQZEVXbMDoHDwVN2tF' es el ID de la lista de reproducción del Top 10 Global de Spotify

# Itera a través de las canciones y muestra la información de cada una
for track_info in results['items']:
    track = track_info['track']
    print(f"Nombre de la canción: {track['name']}")
    print(f"Artista(s): {', '.join([artist['name'] for artist in track['artists']])}")
    print(f"Álbum: {track['album']['name']}")
    print(f"URL de la canción: {track['external_urls']['spotify']}")
    print("\n")
