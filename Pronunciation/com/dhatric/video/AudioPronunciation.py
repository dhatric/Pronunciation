from gtts import gTTS
import requests
from WordDetails import Word
import time

output_audio_directory='../../../output/audio/'
google_url='http://ssl.gstatic.com/dictionary/static/sounds/de/0/'

def removeSpecialCharacters(string):
        return ''.join(e for e in string if e.isalnum())
    
def createAudio(wordObject):
    time.sleep(3)
    #absolutePathAudio=createAudioFromGoogle(wordObject)
    absolutePathAudio="NOTFOUND"
    if absolutePathAudio == "NOTFOUND":
        #print "wordObject %s not found in google",wordObject.get_word()
        absolutePathAudio=createAudioFromTTS(wordObject)
    return absolutePathAudio

def createAudioFromTTS(wordObject):
    tts = gTTS(text=wordObject.get_word(), lang='en')
    absolutePathAudio=output_audio_directory+removeSpecialCharacters(wordObject.get_word()[:20])+".mp3"
    tts.save(absolutePathAudio)
    return absolutePathAudio

def createExampleAudioFromTTS(example_sentense):
    time.sleep(3)
    tts = gTTS(text=example_sentense, lang='en')
    absolutePathAudio=output_audio_directory+removeSpecialCharacters(example_sentense[:20].encode('utf8'))+".mp3"
    tts.save(absolutePathAudio)
    return absolutePathAudio

def createAudioFromGoogle(wordObject):
    absolutePathAudio=output_audio_directory+removeSpecialCharacters(wordObject.get_word()[:20])+".mp3"
    wordUrl=google_url+wordObject.get_word().lower().encode('utf8')+".mp3"
    request = requests.get(wordUrl)
    if request.status_code == 200:
        with open(absolutePathAudio, 'wb') as f:
            for chunk in request:
                f.write(chunk)
    else:
        absolutePathAudio="NOTFOUND"
    return absolutePathAudio
            