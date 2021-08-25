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

    return " ".join(reversed(out))

def add_divider(word_list):
    special_char = ['@','!','#','$','%','^','&','*','(',')','<','>','?','/','}','{','~',':']
    for words in word_list:
        if special_char not in words:
            print(words.append(random.choice(special_char)))

def make_list():
    sentence = "This is my name test testing run"
    s = get_words(sentence)
    
    if ' ' not in s:
        # if there is not spaces infer the sentence then store as list
        words = (infer_spaces(s))
        word_list = words.split()
        
    else:
        # store as list
        word_list = s.split()

    add_divider(word_list)
            
