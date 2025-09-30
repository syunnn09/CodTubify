from yt_dlp import YoutubeDL
from typing import Callable

option = {
    'final_ext': 'mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'nopostoverwrites': False,
        'preferredcodec': 'mp3',
        'preferredquality': '5'
    }],
    'outtmpl': 'src/backend/temp_audio/%(title)s.%(ext)s',
    'ffmpeg_location': 'src/backend/Download_process/ffmpeg.exe',
    'progress_hooks': [],
}

def download_song(link, completion: list[Callable]=None):
    if completion is None:
        completion = []
    option['progress_hooks'] = completion

    try:
        with YoutubeDL(option) as ydl:
            ydl.download([link])
    except:
        print(Exception)
        pass

