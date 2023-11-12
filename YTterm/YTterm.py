from colorama import init as colorama_init
from colorama import Fore
from colorama import Back
from colorama import Style
from rgb2ansi import color
import threading
from ascii_magic import AsciiArt
import os
import ffmpeg
import numpy
import time
import signal
from PIL import ImageEnhance
from pytube import YouTube
import winsound
def audio_thread():
    filename = 'yt-tmp.wav' 
    winsound.PlaySound(filename, winsound.SND_FILENAME)
colorama_init()
os.system('cls||clear')
posx=0
posy=0
print("")
print(f"[[ Welcome to {Back.WHITE}{Fore.BLACK}You{Back.RED}Tube{Style.RESET_ALL}! ]]")
print("")
print("")
print("Please enter video URL.")
url = input("")
print("\nPlease wait...")
YouTube(url).streams.get_by_resolution("360p").download(filename="yt-tmp.mp4")
YouTube(url).streams.get_audio_only().download(filename="yt-tmp.mp3")
ffmpeg.input('yt-tmp.mp4').filter('fps', fps='15').output('yt-tmp/tmp-%d.jpg', start_number=0).overwrite_output().run()
ffmpeg.input('yt-tmp.mp3').output('yt-tmp.wav').overwrite_output().run()
files = os.listdir("yt-tmp")
lenf = len(files)
print(lenf)
auxthread = threading.Thread(target=audio_thread)
auxthread.daemon = True
auxthread.start()
for i in range(lenf):
    my_art = AsciiArt.from_image('yt-tmp/tmp-' + str(i) + ".jpg")
    print("\n\n\n\n\n\n")
    my_art.to_terminal(columns=200, width_ratio=2)