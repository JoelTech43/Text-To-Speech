from gtts import gTTS
from time import sleep
import os
import pyglet

while True:
    a = input()
    if a == "exit":
        tts = gTTS(text="goodbye", lang='en')
        filename = 'temp.mp3'
        tts.save(filename)

        music = pyglet.media.load(filename, streaming=False)
        music.play()

        sleep(music.duration) #prevent from killing
        os.remove(filename) #remove temperory file
        break
    else:
        tts = gTTS(text=a, lang='en')
        filename = 'temp.mp3'
        tts.save(filename)

        music = pyglet.media.load(filename, streaming=False)
        music.play()

        sleep(music.duration) #prevent from killing
        os.remove(filename) #remove temperory file
