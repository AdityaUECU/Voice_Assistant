from pynput.keyboard import Key, Controller
from time import sleep

keyword = Controller()

def volumeup():
    for i in range(5):
        keyword.press(Key.media_volume_up)
        keyword.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    for i in range(5):
        keyword.press(Key.media_volume_down)
        keyword.release(Key.media_volume_down)
        sleep(0.1)