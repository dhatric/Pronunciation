# -*- coding: utf-8 -*- 

import MySQLdb
import time
import sys

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
    
# Open database connection
db = MySQLdb.connect("localhost","root","","pronunciation" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT wordid,lemma,phonetic from words where wordid=147")
results = cursor.fetchall()
for row in results:
    wordId=row[0]
    word=row[1]
    time.sleep(1)
    print ''+str(wordId)+' '+word + ' ' + row[2]
    print db.escape_string("nou'vembə")
    cursor.execute("update words SET phonetic='%s' where wordid= '%d'" % (db.escape_string("nou'vembə"),3))
db.close()