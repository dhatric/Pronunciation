# -*- coding: utf-8 -*- 

from moviepy.editor import *
import AudioPronunciation
import time
from WordDetails import Word
import sys

width=720
height=460
screensize = (width,height)
midHeight=height/2
output_video_directory='../../../output/video/'
wordWidth=680
othersWidth=680
wordHeight=80
othersHeight=30

def createVideo(wordObject):
    audio_file_path = AudioPronunciation.createAudio(wordObject)
    audio_file=AudioFileClip(audio_file_path)
    audio_file.duration
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    textCollection=[]
    
    txt_word = TextClip(wordObject.get_word(),color='white',font='Algerian',method='label',size=(wordWidth,wordHeight))
    txt_word = txt_word.set_pos('center').set_duration(audio_file.duration)
    textCollection.append(txt_word)
    height_next_element=midHeight+(txt_word.h/2)
    
    print hasattr(wordObject,"phonetic")
    
    if hasattr(wordObject,"phonetic") and (wordObject.get_phonetic() and not wordObject.get_phonetic().isspace()):     
        txt_phonetic = TextClip("Phonetic : "+wordObject.get_phonetic(),color='white',font='Arial-Bold',method='label',size=(othersWidth,othersHeight))
        txt_phonetic = txt_phonetic.set_duration(audio_file.duration).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_phonetic.h
        textCollection.append(txt_phonetic)

    if hasattr(wordObject,"meaning") and (wordObject.get_meaning() and not wordObject.get_meaning().isspace()):     
        txt_meaning = TextClip("Meaning : "+wordObject.get_meaning(),color='white',font='Times-New-Roman-Bold-Italic',method='label',size=(othersWidth,othersHeight))
        txt_meaning  = txt_meaning.set_duration(audio_file.duration).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_meaning.h
        textCollection.append(txt_meaning)
    
    if hasattr(wordObject,"synonyms") and len(wordObject.get_synonyms()) != 0 :
        txt_synonyns = TextClip("Synonyms : "+",".join(wordObject.get_synonyms()),color='white',font='Times-New-Roman-Bold-Italic',method='label',size=(othersWidth,othersHeight))
        txt_synonyns  = txt_synonyns.set_duration(audio_file.duration).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_synonyns.h
        textCollection.append(txt_synonyns)
        
    video = CompositeVideoClip(textCollection,size=screensize,bg_color=(255,174,0))
    filler_video=video
    absoluteVideoFile=output_video_directory+wordObject.get_word()[:20]+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4",audio=audio_file_path)
    print "Merging video files"
    singleInstance = VideoFileClip(absoluteVideoFile)
    videosList=[];
    for i in range(11):
        if (i-2)%3 !=0:
            videosList.append(filler_video.set_start(i*audio_file.duration))
        else:
            videosList.append(singleInstance.set_start(i*audio_file.duration))     
    finalVideo = CompositeVideoClip(videosList)
    finalVideo.write_videofile(absoluteVideoFile,codec="mpeg4")
    return absoluteVideoFile
    
#createVideo("Hi How are you")