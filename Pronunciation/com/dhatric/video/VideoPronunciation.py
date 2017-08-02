from moviepy.editor import *
import AudioPronunciation
import time

screensize = (720,460)
output_video_directory='../../../output/video/'

def createVideo(word):
    audio_file_path = AudioPronunciation.createAudio(word)
    audio_file=AudioFileClip(audio_file_path)
    print audio_file.duration
    txt_word = TextClip(word,fontsize=60,color='white',font='Amiri-Bold')
    txt_word = txt_word.set_pos('center').set_duration(audio_file.duration)
    video = CompositeVideoClip([txt_word],size=screensize)
    absoluteVideoFile=output_video_directory+word[:20]+".mp4"
    video.write_videofile(absoluteVideoFile,fps=60,codec="mpeg4",audio=audio_file_path)
    print "Merging video files"
    singleInstance = VideoFileClip(absoluteVideoFile)
    finalVideo = CompositeVideoClip([singleInstance,singleInstance.set_start(audio_file.duration),singleInstance.set_start(audio_file.duration*2)])
    finalVideo.write_videofile(absoluteVideoFile,fps=60,codec="mpeg4")
    return absoluteVideoFile
    
createVideo("You have to grow from the inside out. None can teach you, none can make you spiritual. There is no other teacher but your own soul.")