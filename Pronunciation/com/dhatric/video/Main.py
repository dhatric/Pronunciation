'''
Created on Aug 2, 2017

@author: gdhatric
'''
import argparse
import time

import UploadPronunciation
import VideoPronunciation
from WordDetails import Word

def populateVideoParameters(wordObject,videoFilePath):
    videoDetails = argparse.Namespace()
    videoDetails.file=videoFilePath
    videoDetails.title="How to pronounce "+wordObject.get_word()
    videoDetails.description="How to pronounce "+wordObject.get_word()
    videoDetails.category="22"
    videoDetails.keywords="pronounce,"+wordObject.get_word()+(",".join(wordObject.get_synonyms()))
    videoDetails.privacyStatus="public"
    videoDetails.logging_level="WARNING"
    videoDetails.noauth_local_webserver=True
    return videoDetails
    
    
if __name__ == '__main__': 
    word1=Word()
    word2=Word()
    word1.set_word("First")
    word1.set_word_id(1)
    word1.set_phonetic("hehehe")
    word1.set_example("This is the first example")
    word1.set_synonyms([])
    wordObjects = [word1]
    for wordObject in wordObjects:
        print "uploading word "+wordObject.get_word()
        videoFilePath=VideoPronunciation.createVideo(wordObject)
        videoDetails=populateVideoParameters(wordObject,videoFilePath)
        UploadPronunciation.uploadToYoutube(videoDetails)
        time.sleep(3)
       
    