from voice import VoiceGenerator
from downloader import download_audio

if __name__ == '__main__':
    file_path = download_audio(
        "https://www.youtube.com/watch?v=M7uo5jmFDUw&ab_channel=Fireship")

    # file_name = r'Erlang in 100 Seconds.mp3'

    voice = VoiceGenerator(file_path)
    voice.generate_audio(
        "Foodi. A food management app built with JavaFX. Famous for its clean UI and ease of use.")
