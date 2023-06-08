from collections import Counter
import pandas as pd
import numpy as np
import re

words_list = []
with open("words.txt","r",encoding="utf8") as file:
    file_data = file.read()
    #file_data = file_data.lower()
    words_list = re.findall('\w+', file_data) # find all words matching a single letter or more

dict = set(words_list)
print(f"The first 10 words in our dictionary are: \n{words_list[0:20]}")
print(f"The dictionary has {len(dict)} words ")

def get_count(words):
    word_count_dict = {}
    for i in words:
        if i in word_count_dict:
            word_count_dict[i]+=1
        else:
            word_count_dict[i] = 1
    return word_count_dict

word_count= get_count(words_list)
#print(word_count_dict)
print(f"There are {len(word_count)} key values pairs")

# calculate the probability

def word_probability(word_count_dict):
    probs = {}
    for i in word_count_dict.keys():
        probs[i] = word_count_dict[i]/ sum(word_count_dict.values())
    return probs

# Edit word functions

def insert(word): # insert letter
    insert_letters = []
    split_letter = []
    for i in range(len(word)+1):
        split_letter.append((word[0:i],word[i:]))
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for a,b in split_letter:
        for i in letters:
            insert_letters.append(a+i+b)
    return insert_letters

#print(insert("trash"))

def delete(word): # removes a letter from the word
    delete_letters = []
    split_letter = []
    for i in range(len(word)+1):
        split_letter.append((word[0:i],word[i:]))
    for a,b in split_letter:
        delete_letters.append(a+b[1:])
    return delete_letters

#print(delete("trash"))

def swap(word): # removes a letter from the word
    swap_letters = []
    split_letter = []
    for i in range(len(word)+1):
        split_letter.append((word[0:i],word[i:]))
    for a,b in split_letter:
       if (len(b)>=2):
           swap_letters.append(a+b[1]+b[0]+b[2:])
    return swap_letters

def replace(word): # insert letter
    replace_letters = []
    split_letter = []
    for i in range(len(word)+1):
        split_letter.append((word[0:i],word[i:]))
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for a,b in split_letter:
        for i in letters:
            replace_letters.append(a+i+b[1:])
    return replace_letters

# combining the edits function

def edit_one_letter(word, allow_switches=True):
    edit_set1 = set()
    edit_set1.update(delete(word))
    if allow_switches:
        edit_set1.update(swap(word))
    edit_set1.update(replace(word))
    edit_set1.update(insert(word))
    return edit_set1



# edit two letters
def edit_two_letters(word, allow_switches=True):
    edit_set2 = set()
    edit_one = edit_one_letter(word, allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w, allow_switches=allow_switches)
            edit_set2.update(edit_two)
    return edit_set2


# get corrected word
def word_corrections(word, probs, vocab, n=2):
    suggested_word = []
    best_suggested = []
    suggested_word = list(
        (word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(
            vocab))
    best_suggested = [[s, probs[s]] for s in list(reversed(suggested_word))]
    return best_suggested


my_word = input("Enter a word:")
probs = word_probability(word_count)
tmp_corrections = word_corrections(my_word, probs, dict, 2)
for i, word_prob in enumerate(tmp_corrections):
    print(f"suggested word {i}: {word_prob[0]}, probability : {word_prob[1]:.6f}")