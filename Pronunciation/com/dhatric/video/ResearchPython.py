#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from WordDetails import Word

if __name__ == '__main__':
    word1=Word()
    word1.set_word("First")
    word1.set_word_id(1)
    word1.set_phonetic("hehehe")
    word1.set_example("This is the first example")
    synonym=[]
    #synonym.append("modatidi")
    #synonym.append("rendodi")
    word1.set_synonyms(synonym)
    
    print word1.get_word()
    print word1.get_phonetic()
    print word1.get_example()
    print word1.get_word_id()
    
    myString = ",".join(word1.get_synonyms())
    print myString
    
    