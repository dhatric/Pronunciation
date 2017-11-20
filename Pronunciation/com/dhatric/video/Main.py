# -*- coding: utf-8 -*- 

import argparse
import time
import sys
import UploadPronunciation
import VideoPronunciation
from WordDetails import Word
import MySQLdb
import WordDataExtractor
import re

def populateVideoParameters(wordObject,videoFilePath):
    videoDetails = argparse.Namespace()
    videoDetails.file=videoFilePath
    videoDetails.title=wordObject.get_word()+": Pronounce "+wordObject.get_word()+" with Meaning, Phonetic, Synonyms and Sentence Examples"
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
    generic_desc="This video shows pronunciation of "+word+" in a sentence, "+ word +" meaning, "+ word +" definition, "+word +" phonetic, "+word +" synonym and "+word +" example\n"
    if hasattr(wordObject,"meaning"):
        generic_desc=generic_desc+"\n"+word+" Definition/Meaning : "+wordObject.get_meaning()
    if hasattr(wordObject,"phonetic"):
        generic_desc=generic_desc+"\n"+word+" Phonetic : "+wordObject.get_phonetic()
    if hasattr(wordObject,"synonyms"):
        generic_desc=generic_desc+"\n"+word+" Synonyms : "+wordObject.get_synonyms()
    if hasattr(wordObject,"example") and len(wordObject.get_example()) > 0 :
        examples=word+" Examples : "
        counter=0 
        for example in wordObject.get_example(): 
            examples=examples +"\n"+ re.sub('[<>]+','',example)
            counter+=1
            if counter >2:
                    break  
        generic_desc=generic_desc+"\n"+examples
    generic_desc=generic_desc+"\n\n"+"1,00,000 words with definition, phonetic and examples are available at  http://www.dictionguru.com"
    print generic_desc
    return generic_desc
    
    
    
def getKeywordsWithSEO(wordObject):
    word=wordObject.get_word()
    keyword=["pronounce "+word, word+" Pronunciation ","spell "+word, word+" spelling ","example "+word ,"usage "+word,word+" usage"]  
    keyword.append(word+ " in a sentence")
    keyword.append(word+ " Example")
    keyword.append("Example "+word)
    keyword.append(word+ " Phonetic")
    keyword.append("Phonetic " +word)
    keyword.append(word+ " synonym")
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
    cursor.execute("SELECT wordid,lemma from words WHERE lemma  REGEXP '^[a-zA-Z]*$' and success !='true' and wordid NOT IN (146302,142732) ORDER by wordid DESC " )
    results = cursor.fetchall()
    counter=0
    for row in results:
        counter=counter+1
        if counter>20:
            exit("20 videos are already uploaded")
        time.sleep(0.01)
        wordObject=Word()
        wordObject.set_word(row[1])
        wordObject.set_word_id(row[0])
        print row[0],row[1],counter
        wordObject = WordDataExtractor.populateWordObject(wordObject,db)
        print row[1]+' got the meaning, synonym and examples'
        videoFilePath=VideoPronunciation.createVideo(wordObject)
        videoDetails=populateVideoParameters(wordObject,videoFilePath)
        videoId=UploadPronunciation.uploadToYoutube(videoDetails,wordObject)
        print "video id saving in DB",videoId
        cursor.execute("update words SET success='%s',videoId='%s' where wordid= '%s'" % ("true",videoId,wordObject.get_word_id())) 
        time.sleep(3)
    db.close()  
    