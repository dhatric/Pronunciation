# -*- coding: utf-8 -*- 

'''
Created on Aug 2, 2017

@author: gdhatric
'''
from moviepy.editor import *
import sys
from WordDetails import Word

output_video_directory='../../../output/video/'
width=720
height=460
screensize = (width,height)
midHeight=height/2

if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    textCollection=[]
    wordObject=Word()
    wordObject.set_word("counterfeit")
    wordObject.set_word_id(1)
    wordObject.set_phonetic("Phonetic : kaʊntəfɪt,ˈkaʊntəfiːt")
    wordObject.set_example("This is the first example")
    #wordObject.set_synonyms(["Synonyms","fake"])
    wordObject.set_meaning("Meaning : made in exact imitation of something valuable with the intention to deceive or defraud.")
    
    txt_word = TextClip(wordObject.get_word(),color='white',font='Algerian',method='label',size=(680,80))
    txt_word = txt_word.set_pos('center').set_duration(15)
    textCollection.append(txt_word)
    height_next_element=midHeight+(txt_word.h/2)
    
    print hasattr(wordObject,"phonetic")
    
    if hasattr(wordObject,"phonetic") and (wordObject.get_phonetic() and not wordObject.get_phonetic().isspace()):     
        txt_phonetic = TextClip(wordObject.get_phonetic(),color='white',font='Arial-Bold',method='label',size=(680,20))
        txt_phonetic = txt_phonetic.set_duration(15).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_phonetic.h
        textCollection.append(txt_phonetic)

    if hasattr(wordObject,"meaning") and (wordObject.get_meaning() and not wordObject.get_meaning().isspace()):     
        txt_meaning = TextClip(wordObject.get_meaning(),color='white',font='Times-New-Roman-Bold-Italic',method='label',size=(680,20))
        txt_meaning  = txt_meaning.set_duration(15).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_meaning.h
        textCollection.append(txt_meaning)
    
    if hasattr(wordObject,"synonyms") and len(wordObject.get_synonyms()) != 0 :
        txt_synonyns = TextClip(",".join(wordObject.get_synonyms()),color='white',font='Times-New-Roman-Bold-Italic',method='label',size=(680,20))
        txt_synonyns  = txt_synonyns.set_duration(15).set_pos(('center',height_next_element))
        height_next_element=height_next_element+txt_synonyns.h
        textCollection.append(txt_synonyns)
    
    video = CompositeVideoClip(textCollection,size=screensize,bg_color=(255,174,0))
    absoluteVideoFile=output_video_directory+wordObject.get_word()[:20]+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4")