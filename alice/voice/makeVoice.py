import os
import speech_recognition as sr

from gtts import gTTS
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# my_text = 'are you ok'
# audio = gTTS(text=my_text, lang='en', slow=False)
# audio.save('/home/nasrul/Documents/GitHub/Alice/alice/voice/Alice_voice/question.mp3')

def convwav(data):
    sound = AudioSegment.from_mp3(data)
    sound.export('convmp3.wav', format='wav')

def TxtToSpeach(talk):      
    audio_file = talk
        
    audio = gTTS(text=audio_file, lang='en', slow=False)
    audio.save('/home/nasrul/Python/Alice/voice/Alice_voice/womenTalk.mp3')

def SpeachtoTxt():
    r = sr.Recognizer()
    
    with sr.AudioFile('female.wav') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)