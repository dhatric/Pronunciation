'''
Created on Aug 2, 2017

@author: gdhatric
'''
import argparse
import time

import UploadPronunciation
import VideoPronunciation


def populateVideoParameters(word,videoFilePath):
    videoDetails = argparse.Namespace()
    videoDetails.file=videoFilePath
    videoDetails.title="How to pronounce "+word
    videoDetails.description="How to pronounce "+word
    videoDetails.category="22"
    videoDetails.keywords="pronounce,"+word
    videoDetails.privacyStatus="public"
    videoDetails.logging_level="WARNING"
    videoDetails.noauth_local_webserver=True
    return videoDetails
    
    
if __name__ == '__main__': 
    words = ["hello how are you","I will kill you","PO bey","lets see","fuck off"]
    for word in words:
        print "uploading word "+word
        videoFilePath=VideoPronunciation.createVideo(word)
        videoDetails=populateVideoParameters(word,videoFilePath)
        UploadPronunciation.uploadToYoutube(videoDetails)
        time.sleep(3)
       
    