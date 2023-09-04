"""

/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis

 API que utlice.
 * https://spotipy.readthedocs.io/en/2.22.1/
 
 */
 
"""
# Importar librerias
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from prettytable import PrettyTable

def obtener_canciones_top(client_id, client_secret, playlist_tracks, cantidad_canciones=None):
    """
    Obtiene y muestra las canciones y artistas de una lista de reproducción de Spotify.

    Args:
        client_id (str): El ID de la aplicación de Spotify.
        client_secret (str): El secreto de la aplicación de Spotify.
        playlist_tracks (str): La URL o el ID de la lista de reproducción de Spotify a consultar.
        cantidad_canciones (int, opcional): La cantidad de canciones a mostrar (por defecto, todas).

    Returns:
        None: La función imprime las canciones y artistas en la consola.

    Ejemplo de uso:
        obtener_canciones_top('TU_CLIENT_ID', 'TU_CLIENT_SECRET', '37i9dQZEVXbMDoHDwVN2tF')
        
    """
  
    # Paso 1: Configura tus credenciales de la aplicación de Spotify
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Paso 2: Obtiene las canciones del Top Global
    top_global_tracks = sp.playlist_tracks(playlist_tracks)

    # Paso 3: Crea una tabla para mostrar las canciones y artistas con un índice
    table = PrettyTable()
    table.field_names = ["Índice", "Nombre de la canción", "Artistas"]

    if cantidad_canciones is None:
        cantidad_canciones = len(top_global_tracks['items'])

    for index, track in enumerate(top_global_tracks['items'][:cantidad_canciones], start=1):
        # Obtiene el nombre de la canción
        track_name = track['track']['name']

        # Obtiene los nombres de los artistas y los convierte en una cadena separada por comas
        artists = [artist['name'] for artist in track['track']['artists']]
        artists_str = ', '.join(artists)

        # Agrega una fila a la tabla con el índice
        table.add_row([index, track_name, artists_str])

    # Imprime la tabla formateada
    print(table)
