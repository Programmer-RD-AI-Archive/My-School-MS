import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import os  # to remove created audio files


class person:
    name = ""

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()  # initialise a recogniser
# listen for audio and convert it to text:
def record_audio():
    with sr.AudioFile("./example.wav") as source:  # microphone as source
        audio = r.listen(source)  # listen for the audio via source
        voice_data = r.recognize_google(audio)  # convert audio to text


# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")  # text to speech(voice)
    audio_file = "./example.wav"
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(f"kiri: {audio_string}")  # print what app said
    # os.remove(audio_file)  # remove audio file


# speak("audio string")
record_audio()
