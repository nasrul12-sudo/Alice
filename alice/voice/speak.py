import speech_recognition as sr
import os
import pyttsx3


from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def first():
    file = AudioSegment.from_file('/home/nasrul/Documents/GitHub/Alice/alice/voice/Alice_voice/womenTalk.mp3')
    play(file)    

