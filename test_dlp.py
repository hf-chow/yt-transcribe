import os
import shutil
import yt_dlp as ytd

URL = "https://www.youtube.com/watch?v=BpcemabDB3E&ab_channel=TimDessaint"
temp = "temp"

def create_temp_dir(destination):
    if destination not in os.listdir():
        print(os.listdir())
        os.mkdir(destination)
    else:
        return

def clean_up(destination):
    cwd = os.getcwd()
    path = os.path.join(cwd, destination)
    shutil.rmtree(path)

def download(target, destination):
    os.system("yt-dlp -P {destination} {target}"
              .format(destination=destination, target=target))

create_temp_dir(temp)
download(target=URL, destination=temp)
clean_up(temp)
