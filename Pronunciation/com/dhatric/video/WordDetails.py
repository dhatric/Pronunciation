'''
Created on Aug 9, 2017

@author: gdhatric
'''

class Word:

    def get_word_id(self):
        return self.wordId


    def set_word_id(self, value):
        wordId = value


    def del_word_id(self):
        del self.wordId


    def get_word(self):
        return self.word


    def get_phonetic(self):
        return self.phonetic


    def get_synonyms(self):
        return self.synonyms


    def get_example(self):
        return self.example

    
    def get_meaning(self):
        return self.meaning
    
    def set_word(self, value):
        self.word = value


    def set_phonetic(self, value):
        self.phonetic = value


    def set_synonyms(self, value):
        self.synonyms = value


    def set_example(self, value):
        self.example = value

    def set_meaning(self, value):
        self.meaning = value
        
    def del_word(self):
        del self.word


    def del_phonetic(self):
        del self.phonetic


    def del_synonyms(self):
        del self.synonyms


    def del_example(self):
        del self.example
        
    def del_meaning(self):
        del self.meaning    

