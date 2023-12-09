import os
import threading
from pygame import mixer

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
mixer.init()

def Play(path, volume, loop):
    mixer.music.load(path)
    mixer.music.set_volume(volume)
    if loop:
        mixer.music.play(-1)
    else:
        mixer.music.play()

class Play_Sound_pygame_Now:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": 'comfyui.mp3'}),
                "volume": ("FLOAT", {"default": 1, "min": 0.0, "max": 1.0, "step": 0.01}),
                "loop": ("BOOLEAN", {"default": False}),
                "trigger": ("BOOLEAN", {"default": True}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "do_playsound"
    OUTPUT_NODE = True
    CATEGORY = "MicrosoftSpeech_TTS"

    def do_playsound(self, path, volume, loop, trigger):

        print(f"play sound: path={path},volume={volume},loop={loop},trigger={trigger}")
        if trigger:
            t = threading.Thread(target=Play(path, volume, loop))
            t.start()

        return {}


NODE_CLASS_MAPPINGS = {
    "Play Sound (loop) ": Play_Sound_pygame_Now
}
