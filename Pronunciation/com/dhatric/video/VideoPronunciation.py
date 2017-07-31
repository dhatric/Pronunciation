from moviepy.editor import *
import AudioPronunciation

screensize = (720,460)
output_audio_directory='../../../output/video/'

def createVideo(word):
    audio_file = AudioPronunciation.createAudio(word)
    txt_word = TextClip(word,fontsize=60,color='white',font='Amiri-Bold')
    txt_word = txt_word.set_pos('center').set_duration(10)
    video = CompositeVideoClip([txt_word],size=screensize)
    video.write_videofile(output_audio_directory+word+".mp4",fps=60,codec="mpeg4",audio=audio_file)
    
    
createVideo("welcome Giri")    