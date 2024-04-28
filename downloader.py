import yt_dlp
import os
from constants import VIDEO_AUDIO_DIRECTORY


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
    title = get_video_title(youtube_url)

    file_name = title + '.mp3'

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
        'outtmpl': os.path.join(VIDEO_AUDIO_DIRECTORY, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download audio
        ydl.download([youtube_url])

    # Get the file name

    return os.path.join(VIDEO_AUDIO_DIRECTORY, file_name)


# video_url = "https://www.youtube.com/watch?v=M7uo5jmFDUw&ab_channel=Fireship"
# download_audio(video_url)
