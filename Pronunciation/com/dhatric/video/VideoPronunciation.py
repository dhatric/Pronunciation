from moviepy.editor import *
import AudioPronunciation
import time

screensize = (720,460)
output_video_directory='../../../output/video/'

def createVideo(word):
    audio_file = AudioPronunciation.createAudio(word)
    txt_word = TextClip(word,fontsize=60,color='white',font='Amiri-Bold')
    txt_word = txt_word.set_pos('center').set_duration(4)
    video = CompositeVideoClip([txt_word],size=screensize)
    absoluteVideoFile=output_video_directory+word+".mp4"
    video.write_videofile(absoluteVideoFile,fps=60,codec="mpeg4",audio=audio_file)
    time.sleep(5)
    singleInstance = VideoFileClip(absoluteVideoFile)
    finalVideo = CompositeVideoClip([singleInstance,singleInstance.set_start(4),singleInstance.set_start(8)])
    finalVideo.write_videofile(absoluteVideoFile,fps=60,codec="mpeg4")
    
createVideo("Check")