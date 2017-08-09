# -*- coding: utf-8 -*- 

'''
Created on Aug 2, 2017

@author: gdhatric
'''
from moviepy.editor import *
import sys

output_video_directory='../../../output/video/'
width=720
height=460
screensize = (width,height)
midHeight=height/2

if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    word = "counterfeit"
    phonetic = "Phonetic : kaʊntəfɪt,ˈkaʊntəfiːt"
    meaning="Meaning : made in exact imitation of something valuable with the intention to deceive or defraud."
    synonyns="Synonyms : fake"
    txt_word = TextClip(word,color='white',font='Algerian',method='label',size=(680,80))
    txt_word = txt_word.set_pos('center').set_duration(15)
    
    height_phonetic=midHeight+(txt_word.h/2)
    txt_phonetic = TextClip(phonetic,color='white',font='Arial-Bold',method='label',size=(680,20))
    txt_phonetic = txt_phonetic.set_duration(15).set_pos(('center',height_phonetic))
    
    height_meaning=height_phonetic+(txt_phonetic.h)
    txt_meaning = TextClip(meaning,color='white',font='Times-New-Roman-Bold-Italic',method='label',size=(680,20))
    txt_meaning  = txt_meaning.set_duration(15).set_pos(('center',height_meaning))
    
    height_synonyns=height_meaning+(txt_meaning.h)
    txt_synonyns = TextClip(synonyns,color='white',font='Times-New-Roman-Bold-Italic',method='label',size=(680,20))
    txt_synonyns  = txt_synonyns.set_duration(15).set_pos(('center',height_synonyns))
    
    video = CompositeVideoClip([txt_word,txt_phonetic,txt_meaning,txt_synonyns],size=screensize,bg_color=(255,174,0))
    absoluteVideoFile=output_video_directory+word[:20]+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4")