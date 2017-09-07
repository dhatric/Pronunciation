# -*- coding: utf-8 -*-
import sqlite3

import PhoneticExtractor

if __name__ == '__main__':
    IPA_CMU = PhoneticExtractor.getIPA_CMU("Hello World")
    print IPA_CMU
    print(PhoneticExtractor.get_final(IPA_CMU))
    print "done"