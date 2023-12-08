import sys
import os
import threading
from arcade import load_sound, play_sound

class Sound:

    def play(self, file_name, volume):
        sound = load_sound(file_name)
        play_sound(sound, volume)


def Play(path, volume):
    s = Sound()
    s.play(path, volume)

class Play_Sound_Now():

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": 'comfyui.mp3'}),
                "volume": ("FLOAT", {"default": 1, "min": 0.0, "max": 1.0, "step": 0.01}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "do_playsound"
    OUTPUT_NODE = True
    CATEGORY = "MicorsoftSpeech_TTS"

    def do_playsound(self, path, volume):
        t = threading.Thread(target=Play(path, volume))
        t.start()
        return {"ui": {"text": ("",)}}


NODE_CLASS_MAPPINGS = {
    "Play Sound": Play_Sound_Now
}
