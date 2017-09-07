'''
Created on Aug 8, 2017

@author: gdhatric
'''
import requests
import unicodedata

if __name__ == '__main__':
    request = requests.post('http://texttophonetic.appspot.com/ipa',data={'c':'hello how are you'})
    print type(request.text)
    print request.text.decode('unicode-escape')
