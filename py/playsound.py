import threading
from arcade import load_sound


def Play(path, volume, speed):
    s = load_sound(path)
    s.play(volume, 0, False, speed)

class Play_Sound_Now:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": 'comfyui.mp3'}),
                "volume": ("FLOAT", {"default": 1, "min": 0.0, "max": 1.0, "step": 0.01}),
                "speed": ("FLOAT", {"default": 1, "min": 0.1, "max": 2.0, "step": 0.1}),
                "trigger": ("BOOLEAN",{"default": True}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "do_playsound"
    OUTPUT_NODE = True
    CATEGORY = "MicrosoftSpeech_TTS"

    def do_playsound(self, path, volume, speed, trigger):

        print(f"play sound: path={path},volume={volume},speed={speed},trigger={trigger}")
        if trigger:
            t = threading.Thread(target=Play(path, volume, speed))
            t.start()

        return {}


NODE_CLASS_MAPPINGS = {
    "Play Sound": Play_Sound_Now
}
