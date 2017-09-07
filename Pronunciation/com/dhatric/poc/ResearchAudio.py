'''
Created on Aug 2, 2017

@author: gdhatric
'''
import urllib
import httplib
import requests
if __name__ == '__main__':
    request = requests.get('http://ssl.gstatic.com/dictionary/static/sounds/de/0/exaggerate.mp3')
    if request.status_code == 200:
         with open("exaggerate.mp3", 'wb') as f:
             for chunk in request:
                 f.write(chunk)
    else:
        print('Web site does not exist') 
    

