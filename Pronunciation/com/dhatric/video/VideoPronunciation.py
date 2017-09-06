# -*- coding: utf-8 -*- 

from moviepy.editor import *
import AudioPronunciation
import time
from WordDetails import Word
import sys

width=1600
height=720
screensize = (width,height)
midHeight=height/2
output_video_directory='../../../output/video/'
output_audio_directory='../../../output/audio/'
wordWidth=width-40
othersWidth=width-40
wordHeight=height/7
othersHeight=height/20
buffer_space=10
website_height=height-120

def getSynonymHeightMethod(wordObject):
    synonym_length= len(wordObject.get_synonyms())
    print synonym_length
    synonymWordHeight=othersHeight
    method='label'
    if synonym_length > 100 :
        synonymWordHeight=synonymWordHeight+8
        method='caption'
    elif  synonym_length > 200 :
        synonymWordHeight=synonymWordHeight+12
        method='caption'
    return synonymWordHeight ,method 

def createVideo(wordObject):
    audio_file_path = AudioPronunciation.createAudio(wordObject)
    audio_file=AudioFileClip(audio_file_path)
    audio_file.duration
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    textCollection=[]
    
    txt_word = TextClip(wordObject.get_word(),color='white',font='Algerian',method='label',size=(wordWidth,wordHeight))
    txt_word = txt_word.set_pos(('center',150)).set_duration(audio_file.duration)
    textCollection.append(txt_word)
    height_next_element=280
    
    print hasattr(wordObject,"phonetic")
    
    if hasattr(wordObject,"phonetic") and (wordObject.get_phonetic() and not wordObject.get_phonetic().isspace()):     
        txt_phonetic = TextClip("Phonetic : "+wordObject.get_phonetic(),color='white',font='Arial-Bold',method='label',size=(othersWidth,othersHeight))
        txt_phonetic = txt_phonetic.set_duration(audio_file.duration).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_phonetic.h+buffer_space
        textCollection.append(txt_phonetic)

    if hasattr(wordObject,"meaning") and (wordObject.get_meaning() and not wordObject.get_meaning().isspace()):     
        txt_meaning = TextClip("Meaning : "+wordObject.get_meaning(),color='white',font='Times-New-Roman-Bold-Italic',method='label',size=(othersWidth,othersHeight))
        txt_meaning  = txt_meaning.set_duration(audio_file.duration).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_meaning.h+buffer_space
        textCollection.append(txt_meaning)

    if hasattr(wordObject,"synonyms") and len(wordObject.get_synonyms()) != 0 :
        synonymWordHeight,synonymMethod=getSynonymHeightMethod(wordObject)
        txt_synonyns = TextClip("Synonyms : "+wordObject.get_synonyms(),color='white',font='Times-New-Roman-Bold-Italic',method=synonymMethod,size=(othersWidth,synonymWordHeight))
        txt_synonyns  = txt_synonyns.set_duration(audio_file.duration).set_pos(('center',height_next_element))
        textCollection.append(txt_synonyns)
    
    txt_website = TextClip("www.DictionGuru.com",color='white',font='Arial-Bold',method='label',size=(othersWidth,othersHeight))
    txt_website = txt_website.set_pos(('center',website_height)).set_duration(audio_file.duration)
    textCollection.append(txt_website)
    
        
    video = CompositeVideoClip(textCollection,size=screensize,bg_color=(255,174,0))
    filler_video=video
    absoluteVideoFile=output_video_directory+wordObject.get_word()[:20]+".mp4"
    singleInstance = video.set_audio(audio_file)
    videosList=[];
    for i in range(11):
        if (i-2)%3 !=0:
            videosList.append(filler_video.set_start(i*audio_file.duration))
        else:
            videosList.append(singleInstance.set_start(i*audio_file.duration))
    if hasattr(wordObject,"example"):          
        usageVideo=createUsageVideo(wordObject).set_start(CompositeVideoClip(videosList).duration)
        videosList.append(usageVideo)
    finalVideo=CompositeVideoClip(videosList)
    finalVideo.write_videofile(absoluteVideoFile,fps=3,codec="mpeg4")
    return absoluteVideoFile


def createUsageAudio(wordObject):
    audioExampleCollection = []
    audio_start_time = 2
    audio_filler = 2
    counter=0
    for example in wordObject.get_example():
        audio_file_path = AudioPronunciation.createExampleAudioFromTTS(example)
        audio_file = AudioFileClip(audio_file_path)
        print audio_start_time
        audio_file = audio_file.set_start(audio_start_time)
        audio_start_time += audio_filler + audio_file.duration
        audioExampleCollection.append(audio_file)
        counter+=1
        if counter >2:
            break
    
    usageAudio = CompositeAudioClip(audioExampleCollection)
    return usageAudio

def createUsageVideo(wordObject):
    exampleWidth=width-80
    usageAudio = createUsageAudio(wordObject)
    textExampleCollection=[]
    usageHeader="<span size='70000' font='Algerian' foreground='white' ><b>Usage </b></span>"
    txt_usage_header = TextClip(usageHeader,method='pango',size=(exampleWidth,400),print_cmd="true")
    txt_usage_header = txt_usage_header.set_pos(('center',10)).set_duration(usageAudio.duration)
    textExampleCollection.append(txt_usage_header)    
    exampleHeight=180
    if hasattr(wordObject,"example") and len(wordObject.get_example()) > 0 :
        counter=0
        for example in wordObject.get_example():
            txt_usage_word = TextClip("<span size='25000' font='Times-New-Roman-Bold-Italic' foreground='white' >"+example+"</span>",method='pango',size=(exampleWidth,400),print_cmd="true")
            txt_usage_word = txt_usage_word.set_pos(('center',exampleHeight)).set_duration(usageAudio.duration)
            textExampleCollection.append(txt_usage_word)
            exampleHeight+=180
            counter+=1
            if counter >2:
                break
    usageVideo = CompositeVideoClip(textExampleCollection,size=screensize,bg_color=(255,174,0))
    usageVideo=usageVideo.set_audio(usageAudio)
    return usageVideo   
#createVideo("Hi How are you")