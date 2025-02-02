import yt_dlp
import os
from datetime import datetime

url = input("Lütfen video URL'sini girin: ")

if os.name == "nt":
    FFMPEG_PATH = os.path.join('ffmpeg', 'ffmpeg.exe')
    from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER

    with OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        DOWNLOAD_FOLDER = QueryValueEx(
            key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
else:  # For *Nix systems
    FFMPEG_PATH = os.path.join(os.path.dirname(__file__), 'ffmpeg')
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"

# Get current date
current_date = datetime.now().strftime('%Y-%m-%d')

def set_file_properties(d):
    if d['status'] == 'finished':
        file_path = d['filename']
        current_time = datetime.now().timestamp()
        os.utime(file_path, (current_time, current_time))


# Define download options with selected formats
ydl_opts = {
    'format': 'bv*+ba/b',   # Download best video and audio
    'outtmpl': os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
    'ffmpeg_location': FFMPEG_PATH,
    'progress_hooks': [set_file_properties],
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("İndirme Tamamlandı!")

input("Çıkmak için bir tuşa basın...")

""" 'postprocessors': [
        {
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }
    ], """