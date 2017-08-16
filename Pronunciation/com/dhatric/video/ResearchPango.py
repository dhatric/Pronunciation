# -*- coding: utf-8 -*- 

'''
Created on Aug 2, 2017

@author: gdhatric
'''
from moviepy.editor import *
import sys
from WordDetails import Word
import AudioPronunciation

output_video_directory='../../../output/video/'
output_audio_directory='../../../output/audio/'
width=720
height=460
screensize = (width,height)
midHeight=height/2

if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    textCollection=[]
    wordObject=Word()
    usage=['Despite the introduction of a security shield on the new 10 stamp, counterfeits are costing the postal service millions of pounds a year.','The business of counterfeiting appears to be expanding.']
    wordObject.set_example(usage)
    wordObject.set_word("Counterfeit")
    audioCollection=[]
    audio_start_time=2
    audio_filler=2
    for example in wordObject.get_example():
        audio_file_path = AudioPronunciation.createExampleAudioFromTTS(example)
        audio_file=AudioFileClip(audio_file_path)
        print audio_start_time
        audio_file=audio_file.set_start(audio_start_time)
        audio_start_time+=(audio_filler+audio_file.duration)
        audioCollection.append(audio_file)
    
    audio_example_all=CompositeAudioClip(audioCollection)
    auido_example_absolutePath=output_audio_directory+wordObject.get_word()+'examples.mp3'
    #audio_example_all.write_audiofile(auido_example_absolutePath, fps=44100, nbytes=2, buffersize=2000, codec=None, bitrate=None, ffmpeg_params=None, write_logfile=False, verbose=True, progress_bar=True)
    usageHeader="<span size='30000' font='Times-New-Roman-Bold-Italic' foreground='white' ><span foreground='red'><b>Usage </b></span></span>"
    txt_word = TextClip(usageHeader,method='pango',size=(700,400),print_cmd="true")
    txt_word = txt_word.set_pos(('center',10)).set_duration(audio_start_time)
    textCollection.append(txt_word)
    
    exampleHeight=125
    if hasattr(wordObject,"example") and len(wordObject.get_example()) > 0 :
        for example in wordObject.get_example():
            txt_word = TextClip("<span size='20000' font='Times-New-Roman-Bold-Italic' foreground='white' >"+example+"</span>",method='pango',size=(700,400),print_cmd="true")
            txt_word = txt_word.set_pos(('center',exampleHeight)).set_duration(audio_start_time)
            textCollection.append(txt_word)
            exampleHeight+=125
    video = CompositeVideoClip(textCollection,size=screensize,bg_color=(255,174,0))
    video=video.set_audio(audio_example_all)
    absoluteVideoFile=output_video_directory+"luck"+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4",audio=True)