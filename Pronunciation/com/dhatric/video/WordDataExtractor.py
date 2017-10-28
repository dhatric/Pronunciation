# -*- coding: utf-8 -*- 

import urllib2
from bs4 import BeautifulSoup
from WordDetails import Word
import copy
import re
import MySQLdb
import time
import sys
import requests

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8') 
    
def getPhoneticFromApp(content):
    request = requests.post('http://texttophonetic.appspot.com/ipa',data={'c':content})
    phonetic = request.text.decode('unicode-escape')
    return phonetic
    
def getExamples(soup):
    example_only= soup.find('div',attrs={'class':'examples'})
    if example_only is None:
        return None
    example_soap=BeautifulSoup(""+str(example_only),'html.parser')
    examples_array=example_soap.find_all('em')
    if examples_array is None:
        return None
    example_string_array=[]
    for example in examples_array:
        example_str=example.text.replace("‘","").replace("’","")
        example_string_array.append(example_str)
    return example_string_array

def getPhonetic(wordObject,soup):
    phonetic= soup.find('span',attrs={'class':'phoneticspelling'})
    if phonetic is None:
        return getPhoneticFromApp(wordObject.get_word())
    return phonetic.text

def getSynonyms(soup):
    synonyms_only= soup.find('div',attrs={'class':'synonyms'})
    if synonyms_only is None:
        return None
    synonyms_soap=BeautifulSoup(""+str(synonyms_only),'html.parser')
    synonyms=synonyms_soap.find('div',attrs={'class':'exg'})
    if synonyms_soap is None:
        return None  
    return synonyms.text.replace("View synonyms","")

def getMeaning(wordObject,db):
    meaning_cursor = db.cursor()
    meaning_cursor.execute("select ss.definition from  senses as s JOIN synsets as ss ON s.synsetid=ss.synsetid where s.wordid ='%s'",wordObject.get_word_id())
    results = meaning_cursor.fetchall()
    meaning=None
    for row in results:
        meaning=row[0];
        break
    return meaning
 
 
def saveExampleInDB(db,wordObject):
        example_array=wordObject.get_example()
        for example in example_array:
            example_cursor = db.cursor()
            example_cursor.execute("INSERT INTO `oxfordexamples` (`wordId`,`example`) VALUES ('%d','%s')" % (wordObject.get_word_id(),db.escape_string(example))) 

def saveSynonymsInDB(db,wordObject):
        synonyms_cursor = db.cursor()   
        synonyms_cursor.execute("INSERT INTO `oxfordsynonyms` (`wordId`, `synonyms`) VALUES ('%d','%s')" % (wordObject.get_word_id(),db.escape_string(wordObject.get_synonyms()))) 

def savePhoneticInDB(db,wordObject):
        phonetic_cursor = db.cursor() 
        phonetic_cursor.execute("update words SET phonetic='%s' where wordid= '%s'" % (db.escape_string(wordObject.get_phonetic()),wordObject.get_word_id())) 

def removeSpecialCharacters(string):
        return ''.join(e for e in string if e.isalnum())
        
def populateWordObject(wordObject,db):
        page = 'https://en.oxforddictionaries.com/definition/'+wordObject.get_word()
        response = urllib2.urlopen(page)
        if response.read().find('No exact matches') == -1:
            soup = BeautifulSoup(urllib2.urlopen(page), 'html.parser')
            example_array= getExamples(soup)
            phonetic=getPhonetic(wordObject,soup)
            synonyms_comma_sep=getSynonyms(soup)
            if example_array is not None:
                wordObject.set_example(example_array)
                saveExampleInDB(db,wordObject)
            if phonetic is not None:
                wordObject.set_phonetic(phonetic)
                savePhoneticInDB(db,wordObject)
            if synonyms_comma_sep is not None:    
                wordObject.set_synonyms(synonyms_comma_sep)
                saveSynonymsInDB(db,wordObject)
            
        meaning=getMeaning(wordObject,db)
        wordObject.set_meaning(meaning)
        if hasattr(wordObject,"phonetic") :
            wordObject.set_phonetic(getPhoneticFromApp(wordObject.get_word()))
        return wordObject 
    #soup = BeautifulSoup(response, 'html.parser')
