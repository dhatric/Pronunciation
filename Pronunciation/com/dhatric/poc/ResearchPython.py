#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import re


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
   print getSentenceWithEnclosure("learn","I will learn as If never Learned and will be learning for ever.","<B>","</B>")

    