import os
import re
import random

from math import log
from typing import Text
from flask import redirect, render_template, request, session
from functools import wraps


def get_words(sentence):
    """Get the words from input string"""
    s = sentence
    return s

# Stackoverflow https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words

words = open("words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return list(reversed(out))

# add symbol as divider between words insert randomly from preconfig list
def add_divider(words_list):
    special_char = ['@','!','#','$','%','^','&','*','(',')','<','>','?','/','}','{','~',':']
    symbol_add = random.choice(special_char)
    words_list_sym = [s + symbol_add for s in words_list]
    print(words_list_sym)
    return words_list_sym

#abcdefghijklmnopqrstuvwxyz
def rep_char_to_int(words_list_sym):
    replace_words_list_sym = [words.replace('i','1').replace('z','2').replace('e','3').replace('a','4').replace('s','5').replace('b','6').replace('J','7').replace('B','8').replace('g','9') for words in words_list_sym]
    print(replace_words_list_sym)
    return replace_words_list_sym

def capitalize(replace_words_list_sym):
    final_list = [word.capitalize() for word in replace_words_list_sym]
    return ''.join(final_list)

# make the list from user input to pass to other function
def make_list():
    sentence =  'this is my name'
    s = sentence

    if ' ' not in s:
        # if there is not spaces infer the sentence then store as list
        words_list = (infer_spaces(s))
        print(words_list)
        return words_list
        
    else:
        # store as list
        words_list = s.split()
        print(words_list)
        return words_list
            
if __name__=="__main__":
    words_list = make_list()
    words_list_sym = add_divider(words_list)
    replace_words_list_sym = rep_char_to_int(words_list_sym)
    print(capitalize(replace_words_list_sym))
    
    
