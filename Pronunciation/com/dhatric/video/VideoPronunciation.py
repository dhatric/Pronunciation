from moviepy.editor import *
import AudioPronunciation
import time

screensize = (720,460)
output_video_directory='../../../output/video/'

def createVideo(word):
    audio_file_path = AudioPronunciation.createAudio(word)
    audio_file=AudioFileClip(audio_file_path)
    txt_word = TextClip(word,fontsize=80,color='white',font='Algerian')
    txt_word = txt_word.set_pos('center').set_duration(audio_file.duration)
    txt_phonetic = TextClip(word,fontsize=40,color='white',font='Algerian')
    txt_phonetic = txt_phonetic.set_pos((250,260)).set_duration(audio_file.duration)
    video = CompositeVideoClip([txt_word,txt_phonetic],size=screensize,bg_color=(255,174,0))
    filler_video=video
    absoluteVideoFile=output_video_directory+word[:20]+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4",audio=audio_file_path)
    print "Merging video files"
    singleInstance = VideoFileClip(absoluteVideoFile)
    finalVideo = CompositeVideoClip([filler_video,singleInstance.set_start(audio_file.duration),filler_video.set_start(2*audio_file.duration),singleInstance.set_start(3*audio_file.duration),filler_video.set_start(4*audio_file.duration),singleInstance.set_start(5*audio_file.duration)])
    finalVideo.write_videofile(absoluteVideoFile,codec="mpeg4")
    return absoluteVideoFile
    
createVideo("Hi How are you")