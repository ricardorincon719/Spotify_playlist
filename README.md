# Control de Spotify por voz

Este script permite buscar y reproducir playlists de Spotify por voz.

## Cómo usar

1. Copiar `.env.example` a `.env` y completar con tus credenciales
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python3 spotify_playlist.py "rock nacional"`

¿Qué es esto?
Es un script en Python que permite buscar y reproducir playlists de Spotify usando comandos de voz. Está pensado para integrarse con asistentes como PEARL, pero también puede usarse solo desde la terminal.

¿Qué hace exactamente?
Escucha un nombre de playlist (ej: "rock nacional")

Busca en Spotify usando la API oficial

Reproduce la playlist en tu celular (o cualquier dispositivo Spotify Connect activo)

Todo por voz, sin tocar la pantalla

¿Cómo funciona?
Usa la API de Spotify con autenticación OAuth

El token se guarda localmente (solo una vez)

El script busca la playlist y la reproduce en el dispositivo que elijas

Tecnologías usadas
Python 3

requests-oauthlib (autenticación)

python-dotenv (variables de entorno)

Spotify Web API

Cómo probarlo
bash
git clone https://github.com/ricardorincon719/Spotify_playlist.git
cd Spotify_playlist
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Crear archivo .env con tus credenciales
python spotify_playlist.py "rock nacional"
Notas importantes
Necesitás una cuenta Premium de Spotify (el dueño de la app)

La primera vez se abre el navegador para autorizar

El token se guarda y se refresca automáticamente

¿Qué lo hace especial?
Es totalmente local (no depende de servidores externos)

Puede integrarse con asistentes de voz como PEARL

El código es limpio, modular y fácil de modificar

