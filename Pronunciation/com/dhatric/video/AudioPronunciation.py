from gtts import gTTS
import requests

output_audio_directory='../../../output/audio/'
google_url='http://ssl.gstatic.com/dictionary/static/sounds/de/0/'


def createAudio(word):
    absolutePathAudio=createAudioFromGoogle(word)
    if absolutePathAudio == "NOTFOUND":
        print "word %s not found in google",word
        absolutePathAudio=createAudioFromTTS(word)
    return absolutePathAudio

def createAudioFromTTS(word):
    tts = gTTS(text=word, lang='en')
    absolutePathAudio=output_audio_directory+word+".mp3"
    tts.save(absolutePathAudio)
    return absolutePathAudio


def createAudioFromGoogle(word):
    absolutePathAudio=output_audio_directory+word+".mp3"
    wordUrl=google_url+word.lower().encode('utf8')+".mp3"
    request = requests.get(wordUrl)
    if request.status_code == 200:
        with open(absolutePathAudio, 'wb') as f:
            for chunk in request:
                f.write(chunk)
    else:
        absolutePathAudio="NOTFOUND"
    return absolutePathAudio
            