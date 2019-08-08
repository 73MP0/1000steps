#!/bin/python3

def find_longest_word(word_list):  
    longest_word =  max(word_list, key=len)
    return longest_word



def find_longest_word2(word_list):
    longest_word2 = ''
    for word in word_list:
        if len(word) > len(longest_word2):
            longest_word2 = word
        return longest_word2