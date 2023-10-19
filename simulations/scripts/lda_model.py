#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:00:03 2023

@author: ahunos
LDA
"""


import numpy as np
import scipy
import requests

class LDA():
    
    def __init__(self, Words, url):
        self.Words = Words #bag of words
        self.url = url
        
    def fetch_text(self):
        #url_ex = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
        response = requests.get(url= self.url, allow_redirects=True)
        response.raise_for_status() #raise exceptio for https error
        return response.text
    
    def delete_before_marker(self, text, marker):
        #func to remove all line before "ACT 1"
        lines = text.split('\n')
        for index,val_line in enumerate(lines):
            if marker in val_line:
               return '\n'.join(val_line[index:])
        return text
    
    #def function to remove "      *** END OF THE PROJECT GUTENBERG EBOOK ROMEO AND JULIET ***"
    def splitStrings(self, fetched_text):
        import re
        from collections import Counter 
        words_split1 = re.split('; |, |\*|\n|\s|\.|\[|\]', fetched_text)
        words_selSpaces = [item for item in words_split1 if item != '']
        unique_words = set(words_selSpaces) #get unique words
        wordCollection = Counter(words_selSpaces) #get words and their frequencies
        return wordCollection
        
    def bagoWords(self):
        """
        
        #input, url to document or file to book
        
        #action
        #r1. reads input
        #2. remove stop words
        #lematization 
        #creates vector/matrix of words and proportion of each word
        Returns
        -------
        """
        pass
        
    def getDictTokens():
        #get tokens of words to use
        pass
    
    def dirchlet():
        #len of params equal to words in dictionary
        pass
    
    pass


import requests
url_ex = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"

response = requests.get(url= url_ex, allow_redirects=True)
response.raise_for_status()
response.text

small_text=response.text[1:1000]
len(small_text[900:998])
import re

strSplit1 = re.split('; |, |\*|\n|\s|\.|\[|\]', small_text)
strSplit1_noSpace = [it for it in strSplit1 if it != '']
Counter(strSplit1_noSpace)


small_text.split('\n')
small_text_split = small_text.split('\r') #split by sentences
small_text_split =  [i.split(' ') for i in small_text_split]