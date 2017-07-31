from gtts import gTTS

output_audio_directory='../../../output/audio/'
def createAudio(word):
    tts = gTTS(text=word, lang='en')
    absolutePathAudio=output_audio_directory+word+".mp3"
    tts.save(absolutePathAudio)
    return absolutePathAudio
