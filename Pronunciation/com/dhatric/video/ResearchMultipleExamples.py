'''
Created on Sep 15, 2017

@author: gdhatric
'''
from moviepy.editor import *
import AudioPronunciation
import time
from WordDetails import Word
import sys
import re


width=1600
height=720
screensize = (width,height)
midHeight=height/2
output_video_directory='../../../output/video/'
output_audio_directory='../../../output/audio/'
wordWidth=width-40
othersWidth=width-40
wordHeight=height/4
othersHeight=height/20
buffer_space=10
website_height=height-120


def createDynamicExample(wordObject):
    audio_start_time = 2
    audio_filler = 2
    textExampleCollection=[]
    exampleWidth=width-80
    exampleHeight=180
    usageHeader="<span size='70000' font='Algerian' foreground='white' ><b>"+wordObject.get_word()+" Usage </b></span>"
    txt_usage_header = TextClip(usageHeader,method='pango',size=(exampleWidth,400),print_cmd="true")
    txt_usage_header = txt_usage_header.set_pos(('center',10))

    for example in wordObject.get_example():
        audio_file_path = AudioPronunciation.createExampleAudioFromTTS(example)
        audio_file = AudioFileClip(audio_file_path)
        audio_file = audio_file.set_start(audio_start_time)
        txt_usage_word = TextClip("<span size='25000' font='Times-New-Roman-Bold-Italic' foreground='white' >"+example+"</span>",method='pango',size=(exampleWidth,400),print_cmd="true")
        txt_usage_word = txt_usage_word.set_pos(('center',exampleHeight))
        txt_usage_word = txt_usage_word.set_audio(audio_file)
        txt_usage_word = txt_usage_word.set_start(audio_start_time)
        audio_start_time += audio_filler + audio_file.duration
        #txt_usage_word = txt_usage_word.set_duration(PENDING)
        textExampleCollection.append(txt_usage_word)
    audio_end_duration= audio_start_time           
    txt_website = TextClip("www.DictionGuru.com",color='white',font='Arial-Bold',method='label',size=(othersWidth,othersHeight))
    txt_website = txt_website.set_pos(('center',website_height))
    #txt_website = txt_website.set_duration(audio_end_duration)
    #txt_usage_header = txt_usage_header.set_duration(audio_end_duration)
    textExampleCollection.append(txt_usage_header) 
    textExampleCollection.append(txt_website)
    finalExampleCollection=[]        
    for text in textExampleCollection:
        finalExampleCollection.append(text.set_duration(audio_end_duration))
    usageVideo = CompositeVideoClip(finalExampleCollection,size=screensize,bg_color=(72,141,97))
    return usageVideo
    
    
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

    
    usageAudio = CompositeAudioClip(audioExampleCollection)
    return usageAudio

def createUsageVideo(wordObject):
    exampleWidth=width-80
    usageAudio = createUsageAudio(wordObject)
    textExampleCollection=[]
    usageHeader="<span size='70000' font='Algerian' foreground='white' ><b>"+wordObject.get_word()+" Usage </b></span>"
    txt_usage_header = TextClip(usageHeader,method='pango',size=(exampleWidth,400),print_cmd="true")
    txt_usage_header = txt_usage_header.set_pos(('center',10)).set_duration(usageAudio.duration)
    textExampleCollection.append(txt_usage_header)    
    exampleHeight=180
    if hasattr(wordObject,"example") and len(wordObject.get_example()) > 0 :
        counter=1
        for example in wordObject.get_example():
            example=getSentenceWithEnclosure(wordObject.get_word(),example,"<span foreground='red' >","</span>")
            txt_usage_word = TextClip("<span size='25000' font='Times-New-Roman-Bold-Italic' foreground='white' >"+example+"</span>",method='pango',size=(exampleWidth,400),print_cmd="true")
            txt_usage_word = txt_usage_word.set_pos(('center',exampleHeight)).set_duration(usageAudio.duration)
            textExampleCollection.append(txt_usage_word)
            exampleHeight+=150
            counter+=1
            if counter%3 ==0:
                exampleHeight=180
    txt_website = TextClip("www.DictionGuru.com",color='white',font='Arial-Bold',method='label',size=(othersWidth,othersHeight))
    txt_website = txt_website.set_pos(('center',website_height)).set_duration(usageAudio.duration)
    textExampleCollection.append(txt_website)        
    usageVideo = CompositeVideoClip(textExampleCollection,size=screensize,bg_color=(72,141,97))
    usageVideo=usageVideo.set_audio(usageAudio)
    return usageVideo   

def getSentenceWithEnclosure(word,sentence,startEnclosure,closeEnclosure):
    sentense_array= sentence.split(" ")
    sentence_withBold=[]
    for token in sentense_array:
        if re.search(word, token, re.IGNORECASE):
            sentence_withBold.append(startEnclosure+token+closeEnclosure)
        else:
            sentence_withBold.append(token)    
    return ' '.join(sentence_withBold)


if __name__ == '__main__':
     w1 =  Word()
     examples=[];
     examples.append("I am so blue I'm greener than purple.")
     examples.append("I stepped on a Corn Flake, now I'm a Cereal Killer")
     examples.append("Llamas eat sexy paper clips")
     examples.append("On a scale from one to ten what is your favourite colour of the alphabet.")
     examples.append("Everyday a grape licks a friendly cow")
     examples.append("The sparkly lamp ate a pillow then punched Larry.")
     examples.append("What do you think about the magical yellow unicorn who dances on the rainbow with a spoonful of blue cheese dressing?")
     examples.append("Look, a distraction!")
     examples.append("My world is where everybody is a pony and we all eat rainbows and poop butterflies")
     w1.set_example(examples)
     w1.set_word("Dynamic")
     finalVideo=createDynamicExample(w1)
     absoluteVideoFile=output_video_directory+w1.get_word()[:20]+".mp4"
     finalVideo.write_videofile(absoluteVideoFile,fps=3,codec="mpeg4")
     
