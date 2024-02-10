from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x600")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("10837.gif")
    lb1 = Label(root)
    lb1.place(x=0, y=0)
    i = 0
    mixer.music.load("boom-geomorphism-cinematic-trailer-sound-effects-123876.mp3")
    mixer.music.play()

    for img in ImageSequence.Iterator(img):
        img = img.resize((1000, 600))
        img = ImageTk.PhotoImage(img)
        lb1.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()


play_gif()
root.mainloop()
