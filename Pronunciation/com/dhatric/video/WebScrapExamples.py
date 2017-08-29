'''
Created on Aug 29, 2017

@author: gdhatric
'''
import urllib2
from bs4 import BeautifulSoup
page = 'https://en.oxforddictionaries.com/definition/hello'

if __name__ == '__main__':
    response = urllib2.urlopen(page)
    #print response.read()
    soup = BeautifulSoup(response, 'html.parser')

    
def getExamples(soup):
    example_only= soup.find('div',attrs={'class':'examples'})
    example_soap=BeautifulSoup(""+str(example_only),'html.parser')
    examples_array=example_soap.find_all('em')
    for example in examples_array:
        print example.text
    return examples_array

def getPhonetic(soup):
    phonetic= soup.find('span',attrs={'class':'phoneticspelling'})
    return phonetic.text

def getSynonyms(soup):
    synonyms_only= soup.find('div',attrs={'class':'synonyms'})
    synonyms_soap=BeautifulSoup(""+str(synonyms_only),'html.parser')
    synonyms=synonyms_soap.find('div',attrs={'class':'exg'})
    return synonyms.text