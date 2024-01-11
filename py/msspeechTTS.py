import asyncio
import datetime
import edge_tts
import numpy as np
import folder_paths
import os

async def gen_tts(_text, _voice, _rate, filename):
    tts = edge_tts.Communicate(text=_text, voice=_voice, rate=_rate)
    await tts.save(filename)

INIFILE = os.path.join(os.path.dirname(os.path.dirname(os.path.normpath(__file__))), "voicelist.ini")
voice_dict = {}
try:
    print('# 😺dzNodes: MSSpeech TTS: Load voice setting -> ' + INIFILE)
    with open(INIFILE, 'r') as f:
        ini = f.readlines()

        for line in ini:
            if not line.startswith('#') and len(line) > 1:
                api_name = line[: line.find('(')].rstrip()
                gender = line[line.find('(') + 1:-2]
                lang = api_name[:api_name.rfind('-')]
                name = api_name[api_name.rfind('-') + 1:api_name.find('Neural')]
                display_item = lang + ':' + name + '(' + gender + ')'
                voice_dict.update({display_item: api_name})
        print('# 😺dzNodes: MSSpeech TTS: ' + str(len(voice_dict)) + ' voice load successfully.')
except Exception as e:
    print('# 😺dzNodes: MSSpeech TTS: ERROR -> ' + repr(e))


class Text2AudioEdgeTts:
    def __init__(self):
        self.output_dir = os.path.join(folder_paths.get_output_directory(), 'audio')
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    @classmethod
    def INPUT_TYPES(cls):

        VOICES =  list(voice_dict.keys())
        return {
            "required": {
                "voice": (VOICES, ),
                "rate": ("INT", {"default": 0, "min": -200, "max": 200}),
                "filename_prefix": ("STRING", {"default": "comfyUI"}),
                "text": ("STRING", {"multiline": True}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("MP3 file: String",)
    FUNCTION = "text_2_audio"
    OUTPUT_NODE = True
    CATEGORY = "😺dzNodes"

    def text_2_audio(self,voice,filename_prefix,text,rate):
        voice_name = voice_dict[voice]
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
        _datetime = datetime.datetime.now().strftime("%Y%m%d")
        _datetime = _datetime + datetime.datetime.now().strftime("%H%M%S%f")
        file = f"{filename}_{_datetime}_{voice_name}.mp3"
        audio_path=os.path.join(full_output_folder, file)
        _rate = str(rate) + "%" if rate < 0 else "+" + str(rate) + "%"
        print(f"# 😺dzNodes: MSSpeech TTS: Generating voice files, voice=‘{voice_name}’, rate={rate}, audiofile_path='{audio_path}, 'text='{text}'")

        asyncio.run(gen_tts(text,voice_name,_rate,audio_path))

        return {"ui": {"text": "Audio file："+os.path.join(full_output_folder, file),
        'audios':[{'filename':file,'type':'output','subfolder':'audio'}]}, "result": (audio_path, )}


async def edge_tts_text_2_audion(VOICE,TEXT,OUTPUT_FILE) -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

NODE_CLASS_MAPPINGS = {
    "MicrosoftSpeech_TTS": Text2AudioEdgeTts
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MicrosoftSpeech_TTS": "MicrosoftSpeech_TTS"
}
