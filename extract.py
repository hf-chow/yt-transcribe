import subprocess
import os

TEMP_PATH = os.path.join(os.getcwd(), "temp/")

def get_vids(dir):
    vids = []

    for v in os.listdir(dir):
        if ".mp3" in v:
            vids.append(v)
    return vids

def extract_audio(fname):
    command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}.wav".format(fname)
    
    try:
        subprocess.call(command, shell=True)
    except:
        print("""An error occurred while attempting to extract audio from {}, 
              please check if the path is correct or whether ffmpeg has been properly installed""") 

def extract_all(dir=TEMP_PATH):
    vids = get_vids(dir)
    
    for v in vids:
        extract_audio(v)
