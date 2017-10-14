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
    videoDetails.title=wordObject.get_word()+": How to pronounce "+wordObject.get_word()+" with Phonetic and Examples"
    videoDetails.description=getDescriptionWithSEO(wordObject)
    videoDetails.category="27"
    videoDetails.keywords=getKeywordsWithSEO(wordObject)
    videoDetails.privacyStatus="public"
    videoDetails.logging_level="WARNING"
    videoDetails.noauth_local_webserver=True
    videoDetails.still_id=1
    return videoDetails
    

def getDescriptionWithSEO(wordObject):
    word=wordObject.get_word()
    generic_desc="This video shows how to pronounce "+word+" correctly with phonetic and examples on how to use it"
    if hasattr(wordObject,"meaning"):
        generic_desc=generic_desc+"\n"+word+" Definition : "+wordObject.get_meaning()
    if hasattr(wordObject,"phonetic"):
        generic_desc=generic_desc+"\n"+word+" Phonetic : "+wordObject.get_phonetic()
    if hasattr(wordObject,"synonyms"):
        generic_desc=generic_desc+"\n"+word+" Synonyms : "+wordObject.get_synonyms()
    if hasattr(wordObject,"example") and len(wordObject.get_example()) > 0 :
        examples=word+" Examples : "
        counter=0 
        for example in wordObject.get_example(): 
            examples=examples +"\n"+ example
            counter+=1
            if counter >2:
                    break  
        generic_desc=generic_desc+"\n "+examples
    generic_desc=generic_desc+"\n"+" 1,00,000 words with definition, phonetic and examples are available at  www.dictionguru.com"
    return generic_desc
    
    
    
def getKeywordsWithSEO(wordObject):
    word=wordObject.get_word()
    keyword=["pronounce "+word, word+" Pronunciation ","spell "+word, word+" spelling ","example "+word ,"usage "+word,word+" usage"]  
    keyword.append(word+ " Example")
    keyword.append(word+ " Phonetic")
    keyword.append(word+ " synonyms")
    keyword.append("Define "+word)
    keyword.append(word+ " Definition")
    keyword.append(word+ " say")
    keyword.append("How to say "+word)
    return ",".join(keyword)

if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8') 
    db = MySQLdb.connect("localhost","root","","pronunciation" )
    cursor = db.cursor()
    cursor.execute("SELECT wordid,lemma from words WHERE lemma  REGEXP '^[a-zA-Z]*$' and success !='true'" )
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
        videoId=UploadPronunciation.uploadToYoutube(videoDetails,wordObject)
        print "video id saving in DB",videoId
        cursor.execute("update words SET success='%s',videoId='%s' where wordid= '%s'" % ("true",videoId,wordObject.get_word_id())) 
        time.sleep(3)
    db.close()  
    