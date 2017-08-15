#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from WordDetails import Word

duration=2
if __name__ == '__main__':
    for i in range(11):
        if (i-2)%3 !=0:
            print "filler " + str(i*duration)
        else:
            print "withAudio "+str(i*duration)
    
    