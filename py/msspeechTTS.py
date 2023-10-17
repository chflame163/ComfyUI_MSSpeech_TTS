import asyncio
import datetime

import edge_tts
import numpy as np
import folder_paths
import os

async def gen_tts(_text,_voice,_rate,filename):
    tts = edge_tts.Communicate(text = _text, voice = _voice, rate = _rate)
    await tts.save(filename)

class Text2AutioEdgeTts:
    def __init__(self):
        self.output_dir = os.path.join(folder_paths.get_output_directory(), 'audio')
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    @classmethod
    def INPUT_TYPES(cls):
        VOICES=['zh-CN-XiaoxiaoNeural','zh-CN-XiaoyiNeural','zh-CN-YunjianNeural','zh-CN-YunxiNeural','zh-CN-YunxiaNeural',
'zh-CN-YunyangNeural','zh-CN-liaoning-XiaobeiNeural','zh-CN-shaanxi-XiaoniNeural','zh-HK-HiuGaaiNeural',
'zh-HK-HiuMaanNeural','zh-HK-WanLungNeural','zh-TW-HsiaoChenNeural','zh-TW-HsiaoYuNeural','zh-TW-YunJheNeural']
        return {
            "required": {
                "voice": (VOICES, ),
                "rate": ("INT", {"default": 0, "min": -200, "max": 200}),
                "filename_prefix": ("STRING", {"default": "comfyUI"}),
                "text": ("STRING", {"multiline": True})
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("MP3 file: String",)
    FUNCTION = "text_2_autio"
    OUTPUT_NODE = True

    CATEGORY = "MicorsoftSpeech_TTS"

    def text_2_autio(self,voice,filename_prefix,text,rate):
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
        _datetime = datetime.datetime.now().strftime("%Y_%m_%d")
        _datetime = _datetime + "_" + datetime.datetime.now().strftime("%H_%M_%S")
        file = f"{filename}_{_datetime}_{counter:02}.mp3"
        autio_path=os.path.join(full_output_folder, file)
        _rate = str(rate) + "%" if rate < 0 else "+" + str(rate) + "%"
        print(f"MicrosoftSpeech TTS: Generating voice files, voice=‘{voice}’, rate={rate}, audiofile_path='{autio_path}, 'text='{text}'")
        # asyncio.run(edge_tts_text_2_aution(voice,text,autio_path))
        asyncio.run(gen_tts(text,voice,_rate,autio_path))

        return {"ui": {"text": "Audio file saved to："+os.path.join(full_output_folder, file),
        'autios':[{'filename':file,'type':'output','subfolder':'autio'}]}, "result": (autio_path, )}


async def edge_tts_text_2_aution(VOICE,TEXT,OUTPUT_FILE) -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

NODE_CLASS_MAPPINGS = {
    "MicorsoftSpeech_TTS": Text2AutioEdgeTts
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MicorsoftSpeech_TTS": "MicorsoftSpeech_TTS"
}
