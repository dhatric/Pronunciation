# -*- coding: utf-8 -*- 

import argparse
import time
import sys
import UploadPronunciation
import VideoPronunciation
from WordDetails import Word
import MySQLdb
import WordDataExtractor

def populateVideoParameters(wordObject,videoFilePath):
    videoDetails = argparse.Namespace()
    videoDetails.file=videoFilePath
    videoDetails.title="How to pronounce "+wordObject.get_word()
    videoDetails.description="How to pronounce "+wordObject.get_word()
    videoDetails.category="22"
    keywords=" "
    if hasattr(wordObject,"synonyms"):
        keywords=wordObject.get_synonyms()
    videoDetails.keywords="pronounce,"+wordObject.get_word()+keywords
    videoDetails.privacyStatus="public"
    videoDetails.logging_level="WARNING"
    videoDetails.noauth_local_webserver=True
    return videoDetails
    
    
if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8') 
    db = MySQLdb.connect("localhost","root","","pronunciation" )
    cursor = db.cursor()
    cursor.execute("SELECT wordid,lemma from words WHERE lemma  REGEXP '^[a-zA-Z]*$'")
    results = cursor.fetchall()
    for row in results:
        time.sleep(0.01)
        wordObject=Word()
        wordObject.set_word(row[1])
        wordObject.set_word_id(row[0])
        print row[0],row[1]
        wordObject = WordDataExtractor.populateWordObject(wordObject,db)
        videoFilePath=VideoPronunciation.createVideo(wordObject)
        videoDetails=populateVideoParameters(wordObject,videoFilePath)
        #UploadPronunciation.uploadToYoutube(videoDetails)
        time.sleep(3)
    db.close()  
    