# comandos/spotify_playlist.py

import os
import sys
sys.path.append('/home/samsung-ubuntu/MiJarvis')
from utils.spotify_auth import get_spotify_session
from pearl import escuchar, hablar

def ejecutar(nombre_playlist=None):
    """
    Busca y reproduce una playlist por su nombre.
    Si no se proporciona nombre, lo pide por voz.
    """
    try:
        # Si no nos dieron nombre, lo pedimos
        if not nombre_playlist:
            hablar("Decí el nombre de la playlist, che")
            texto, vector, frames = escuchar()
            if not texto:
                return "No entendí el nombre de la playlist"
            nombre_playlist = texto
        
        # Ahora sí, tenemos el nombre
        print(f"🔍 Buscando playlist: {nombre_playlist}")
        
        spotify = get_spotify_session()
        base_url = "https://api.spotify.com/v1"
        
        response = spotify.get(
            f"{base_url}/search",
            params={
                "q": nombre_playlist,
                "type": "playlist",
                "limit": 5
            }
        )
        response.raise_for_status()
        data = response.json()
        
        if not data['playlists']['items']:
            return f"No encontré ninguna playlist llamada '{nombre_playlist}'"
        
        # Tomar la primera playlist
        playlist = data['playlists']['items'][0]
        playlist_uri = playlist['uri']
        playlist_name = playlist['name']
        
        # Obtener dispositivos
        devices_response = spotify.get(f"{base_url}/me/player/devices")
        devices = devices_response.json().get('devices', [])
        
        if not devices:
            return "No hay dispositivos Spotify Connect disponibles"
        
        # Buscar el celular (o usar el primer dispositivo activo)
        target_device = None
        for device in devices:
            if device['is_active']:
                target_device = device
                break
        
        if not target_device:
            target_device = devices[0]
        
        # Transferir y reproducir
        spotify.put(
            f"{base_url}/me/player",
            json={"device_ids": [target_device['id']]}
        )
        spotify.put(
            f"{base_url}/me/player/play",
            json={"context_uri": playlist_uri}
        )
        
        return f"Reproduciendo {playlist_name} en {target_device['name']}, che"
        
    except Exception as e:
        return f"Error con Spotify: {str(e)}"
