#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from WordDetails import Word

duration=2
if __name__ == '__main__':
    string = "Special $#!\" 'characters   spaces 888323"
    string=''.join(e for e in string if e.isalnum())
    print string
    
    