import sqlite3
import io

if __name__ == '__main__':
    conn = sqlite3.connect('C:\Giridhar\Projects\python\Pronunciation\Dictionary Database\WordWeb.db')
    print "Opened database successfully";
    with io.open('utf-8.txt', 'w', encoding='utf-8') as words:
        for title, in conn.execute("select sp.pronunciation from unique_words as uw JOIN sound_pronunciations as sp ON uw.word_id=sp.word"):
            words.write(title)
    print "Operation done successfully";
    conn.close()    