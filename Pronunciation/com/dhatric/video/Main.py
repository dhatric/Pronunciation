# -*- coding: utf-8 -*- 

import argparse
import time
import sys
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
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8') 
    word1=Word()
    word2=Word()
    word1.set_word("CounterFeit")
    word1.set_word_id(1)
    word1.set_phonetic("kaʊntəfiːt")
    word1.set_meaning("made in exact imitation of something valuable with the intention to deceive or defraud.")
    word1.set_synonyms(["fake","forgery","sham","spurious", "bogus", "imitation" ])
    usage=['Despite the introduction of a security shield on the new 10 stamp, counterfeits are costing the postal service millions of pounds a year.','The business of counterfeiting appears to be expanding.']
    word1.set_example(usage)
    wordObjects = [word1]
    for wordObject in wordObjects:
        print "uploading word "+wordObject.get_word()
        videoFilePath=VideoPronunciation.createVideo(wordObject)
        videoDetails=populateVideoParameters(wordObject,videoFilePath)
        #UploadPronunciation.uploadToYoutube(videoDetails)
        time.sleep(3)
       
    