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
    wordObject.set_word("<span size='25000' font='Times-New-Roman-Bold-Italic' foreground='white' ><span foreground='red'><b>counterfeit </b></span>currency that had been passed all over town.counterfeit currency that had been passed all over town</span>")
    txt_word = TextClip(wordObject.get_word(),method='pango',size=(600,400),print_cmd="true")
    txt_word = txt_word.set_pos('center').set_duration(15)
    textCollection.append(txt_word)
    video = CompositeVideoClip(textCollection,size=screensize,bg_color=(255,174,0))
    absoluteVideoFile=output_video_directory+"luck"+".mp4"
    video.write_videofile(absoluteVideoFile,fps=4,codec="mpeg4")