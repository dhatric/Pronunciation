# -*- coding: utf-8 -*- 

import MySQLdb
import time
import requests
import sys

def getPhoneticFromWeb(content):
    request = requests.post('http://texttophonetic.appspot.com/ipa',data={'c':content})
    phonetic = request.text.decode('unicode-escape')
    return phonetic
    

def updateAllWordsWithPhonetic():
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    print sys.getdefaultencoding()
    db = MySQLdb.connect("localhost","root","","pronunciation" )
    cursor = db.cursor()
    cursor.execute("SELECT wordid,lemma from words where phonetic=''")
    results = cursor.fetchall()
    for row in results:
        time.sleep(0.2)
        wordId=row[0]
        word=row[1]
        phonetic = getPhoneticFromWeb(word)
        print str(wordId)  +" " +word+"" + phonetic
        cursor.execute("update words SET phonetic='%s' where wordid= '%s'" % (db.escape_string(phonetic),wordId)) 
           
if __name__ == '__main__':
    updateAllWordsWithPhonetic()