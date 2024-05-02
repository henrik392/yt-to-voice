from voice import VoiceGenerator
from downloader import download_audio

if __name__ == '__main__':
    video_id, file_path = download_audio(
        "https://www.youtube.com/watch?v=S_RorY_FRvo&ab_channel=Fireship")

    # file_name = r'Erlang in 100 Seconds.mp3'

    voice = VoiceGenerator(video_id, file_path)
    voice.generate_audio(
        """
This has been Foodi in 100 seconds. Let me know what you want to see next in the comments. Thanks for watching, and I will see you in the next one.
        """
    )
