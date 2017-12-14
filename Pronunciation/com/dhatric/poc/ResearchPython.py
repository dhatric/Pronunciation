#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import re

def removeSpecialCharacters(string):
        return ''.join(e for e in string if e.isalnum())

def getSentenceWithEnclosure(word,sentence,startEnclosure,closeEnclosure):
    sentense_array= sentence.split(" ")
    sentence_withBold=[]
    for token in sentense_array:
        if re.search(word, token, re.IGNORECASE):
            sentence_withBold.append(startEnclosure+token+closeEnclosure)
        else:
            sentence_withBold.append(token)    
    return ' '.join(sentence_withBold)

duration=2
if __name__ == '__main__':
        examples =[]
        examples.append('1234567896464536')
        examples.append('1234435545324532453554')
        examples.append('12345')
        examples.append('1234567')
        examples.append('123456789')
        examples.sort(key=len)
        for e in examples:
            print e

    