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
    wordObject.set_word("<span size='30000' font='Times-New-Roman-Bold-Italic' foreground='white' ><span foreground='red'><b>Usage </b></span></span>")
    txt_word = TextClip(wordObject.get_word(),method='pango',size=(700,400),print_cmd="true")
    txt_word = txt_word.set_pos(('center',10)).set_duration(15)
    textCollection.append(txt_word)
    wordObject.set_word("<span size='15000' font='Times-New-Roman-Bold-Italic' foreground='white' ><span foreground='red'><b>counterfeit </b></span>currency that had been passed all over town.counterfeit currency that had been passed all over town.counterfeit currency that had been passed all over town.counterfeit currency that had been passed all over town</span>")
    txt_word = TextClip(wordObject.get_word(),method='pango',size=(700,400),print_cmd="true")
    txt_word = txt_word.set_pos(('center',100)).set_duration(15)
    textCollection.append(txt_word)
    txt_word = TextClip(wordObject.get_word(),method='pango',size=(700,400),print_cmd="true")
    txt_word = txt_word.set_pos(('center',200)).set_duration(15)
    textCollection.append(txt_word)
    txt_word = TextClip(wordObject.get_word(),method='pango',size=(700,400),print_cmd="true")
    txt_word = txt_word.set_pos(('center',300)).set_duration(15)
    textCollection.append(txt_word)
    video = CompositeVideoClip(textCollection,size=screensize,bg_color=(255,174,0))
    absoluteVideoFile=output_video_directory+"luck"+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4")