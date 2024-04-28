import json
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save
from dotenv import load_dotenv
from constants import VIDEO_AUDIO_DIRECTORY
import os

load_dotenv()


class VoiceGenerator:
    def __init__(self, file_path: str):
        self.file_path = file_path

        file_name = os.path.basename(file_path)
        self.name = os.path.splitext(file_name)[0]
        self.voice_id = self.get_voice_id()
        self.client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    def clone_voice(self):
        with open("saved_voices.json", "r") as f:
            voices = json.load(f)

        if self.name in voices:
            return voices[self.name]

        file_path = rf'./{self.file_path}'
        cloned_voice = self.client.clone(
            name=self.name,
            description=f"Voice clone from this video: {self.file_path}",
            files=[file_path]
        )

        voice_details = {
            "voice_id": cloned_voice.voice_id,
            "name": cloned_voice.name,
            "description": cloned_voice.description,
        }
        voice_details["voice_id"] = cloned_voice.voice_id

        voices[self.name] = voice_details
        with open("saved_voices.json", "w") as f:
            json.dump(voices, f)

        return voice_details

    def get_voice_id(self):
        return self.clone_voice()["voice_id"]

    def generate_audio(self, text: str):
        audio = self.client.generate(
            text=text,
            voice=self.voice_id
        )

        save(audio, rf'./speech/{self.name}.mp3')
        play(audio)
