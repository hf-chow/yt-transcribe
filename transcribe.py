import openai
import os

def transcribe(fname, dir=TEMP_PATH):
    fpath = os.path.join(dir, fname)
    if ".wav" in fname:
        audio_file = open(fpath, "rb")
        transcript = openai.Audio.translate("whisper-1", audio_file)
    return transcript
