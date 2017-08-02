'''
Created on Aug 2, 2017

@author: gdhatric
'''
import argparse
import time
import VideoPronunciation
import UploadPronunciation

def populateVideoParameters(word,videoFilePath):
    videoDetails = argparse.Namespace()
    videoDetails.file=videoFilePath
    videoDetails.title=word
    videoDetails.description=word
    videoDetails.category="22"
    videoDetails.keywords=word
    videoDetails.privacyStatus="public"
    videoDetails.logging_level="WARNING"
    videoDetails.noauth_local_webserver=True
    return videoDetails
    
if __name__ == '__main__':
    words = ["hi","hello","python","welcome"]
    for word in words:
        print "uploading word "+word
        videoFilePath=VideoPronunciation.createVideo(word)
        videoDetails=populateVideoParameters(word,videoFilePath)
        UploadPronunciation.uploadToYoutube(videoDetails)
        time.sleep(3)
       
    