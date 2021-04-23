import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask=False):

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio , language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlamadım")
        except sr.RequestError:
            speak('sistem çalısmıyor')
        return voice

def response(voice):
    if "nasılsın" in voice:
        speak("iyi sen?")
    if "Merhaba" in voice:
        speak("sana da merhaba")
    if "teşekkürler" in voice:
        speak("ne demek rica ederim")
    if "senin adın ne " in voice:
        speak("bilmiyorum")



    if "arama yap" in voice:
        search = record("ne aramak istiyorsun")
        time.sleep(0.01)
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak(search + "için bulduklarım")
        time.sleep(0.01)
    if "tamamdır" in voice:
        speak("görüşürüz")
        time.sleep(0.01)
        exit()

def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-" + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("nasıl yardımcı olabilirim")
time.sleep(0.01)
while 1:
    voice = record()
    print(voice)
    response(voice)

