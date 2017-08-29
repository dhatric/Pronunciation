'''
Created on Aug 29, 2017

@author: gdhatric
'''
import urllib2
from bs4 import BeautifulSoup
page = 'https://en.oxforddictionaries.com/definition/counterfeit'

if __name__ == '__main__':
    response = urllib2.urlopen(page)
    #print response.read()
    soup = BeautifulSoup(response, 'html.parser')
    example_only= soup.find('div',attrs={'class':'examples'})
    example_soap=BeautifulSoup(""+str(example_only),'html.parser')
    examples=example_soap.find_all('em')
    
    for example in examples:
        print example.text
    #print str().decode('unicode-escape')