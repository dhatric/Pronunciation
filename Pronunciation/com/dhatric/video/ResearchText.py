# -*- coding: utf-8 -*- 

'''
Created on Aug 2, 2017

@author: gdhatric
'''
from moviepy.editor import *
import sys

output_video_directory='../../../output/video/'
screensize = (720,460)

if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    word = "What the hell is going on. I didnt expected this. Very Funny though"
    phonetic = "What the hell is going on. I didnt expected this. Very Funny though "
    txt_word = TextClip(word,color='white',font='Algerian',method='label',size=(720,None))
    txt_word = txt_word.set_pos('center').set_duration(15)
    
    print txt_word.w
    print txt_word.h
    video = CompositeVideoClip([txt_word],size=screensize,bg_color=(255,174,0))
    absoluteVideoFile=output_video_directory+word[:20]+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4")