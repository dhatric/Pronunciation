'''
Created on Aug 2, 2017

@author: gdhatric
'''
from moviepy.editor import *

output_video_directory='../../../output/video/'
screensize = (720,460)

if __name__ == '__main__':
    word = "Counterfeit"
    phonetic = "kawn-tu-fit"
    txt_word = TextClip(word,fontsize=80,color='white',font='Algerian')
    txt_word = txt_word.set_pos('center').set_duration(15)
    txt_phonetic = TextClip(phonetic,fontsize=40,color='white',font='Algerian')
    txt_phonetic = txt_phonetic.set_pos((250,260)).set_duration(15)
    video = CompositeVideoClip([txt_word,txt_phonetic],size=screensize,bg_color=(255,174,0))
    absoluteVideoFile=output_video_directory+word[:20]+".mp4"
    video.write_videofile(absoluteVideoFile,fps=20,codec="mpeg4")