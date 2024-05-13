import yt_dlp
import os
from constants import VIDEO_AUDIO_DIRECTORY
import re


def get_youtube_id(url):
    # This regex pattern works for standard and shortened YouTube URLs
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None


def get_video_title(youtube_url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        return info_dict.get('title', None)


def file_exists(file_name):
    files = os.listdir(VIDEO_AUDIO_DIRECTORY)
    for file in files:
        if file_name in file:
            return True
    return False


def download_audio(youtube_url):
    youtube_id = get_youtube_id(youtube_url)
    file_name = youtube_id + '.mp3'

    if file_exists(file_name):
        print(f"File {file_name} already exists in {VIDEO_AUDIO_DIRECTORY}")
        return file_name

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(VIDEO_AUDIO_DIRECTORY, youtube_id + '.%(ext)s'),
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download audio
        ydl.download([youtube_url])

    # Get the file name

    return os.path.join(VIDEO_AUDIO_DIRECTORY, file_name)
