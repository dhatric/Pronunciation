'''
Created on Aug 9, 2017

@author: gdhatric
'''

class Word:

    def get_word_id(self):
        return self.__wordId


    def set_word_id(self, value):
        self.__wordId = value


    def del_word_id(self):
        del self.__wordId


    def get_word(self):
        return self.__word


    def get_phonetic(self):
        return self.__phonetic


    def get_synonyms(self):
        return self.__synonyms


    def get_example(self):
        return self.__example


    def set_word(self, value):
        self.__word = value


    def set_phonetic(self, value):
        self.__phonetic = value


    def set_synonyms(self, value):
        self.__synonyms = value


    def set_example(self, value):
        self.__example = value


    def del_word(self):
        del self.__word


    def del_phonetic(self):
        del self.__phonetic


    def del_synonyms(self):
        del self.__synonyms


    def del_example(self):
        del self.__example
    
    word = property(get_word, set_word, del_word, "word's docstring")
    phonetic = property(get_phonetic, set_phonetic, del_phonetic, "phonetic's docstring")
    synonyms = property(get_synonyms, set_synonyms, del_synonyms, "synonyms's docstring")
    example = property(get_example, set_example, del_example, "example's docstring")
    wordId = property(get_word_id, set_word_id, del_word_id, "wordId's docstring")
