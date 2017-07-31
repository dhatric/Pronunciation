from gtts import gTTS

output_audio_directory='../../../output/audio/'
def createAudio(word):
    tts = gTTS(text=word, lang='en')
    absolutePathAudio=output_audio_directory+word+".mp3"
    tts.save(absolutePathAudio)
    return absolutePathAudio


#createAudio("counterfeit counterfeit counterfeit counterfeit counterfeit")    
#cwd = os.getcwd()
#print cwd
#print os.path.abspath(os.curdir)
#os.chdir("../../..")
#print os.path.abspath(os.curdir)

