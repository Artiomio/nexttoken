# -*- coding: utf-8 -*-
"""markov wordwise with my own sparse matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oERqeYb5Emy1dIrUNgpg6Zci1xq2a2SP
"""

import numpy as np
import requests
import re
import sys
import time

from tqdm import tqdm
from sparsematrix import SparseMatrix
from enumeratingtokenizer import EnumeratingTokenizer

def clean_html(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext.replace("&nbsp;", "")


def text_brushing(text):
    text = text.replace("--", "—").replace("\r", "").replace("\n", " \n ")
    return text

url = "http://az.lib.ru/t/twen_m/text_1884_the_adventures_of_huckleberry_finn.shtml"
#url = "http://www.lib.ru/LINDGREN/malysh.txt_Ascii.txt"
text = requests.get(url).text



try:
    file_name = sys.argv[1]
except:
    file_name = "warandpeace"

#print(file_name)
#f = open(file_name, "r", encoding="cp1251")
#text = f.read()

tokens_are_words = 1
markov_dim = 2

if tokens_are_words:
    text = clean_html(text)
    text = text.split()
else:
    text = text.replace("\n", "")

    

tknz = EnumeratingTokenizer(text)
text_digitized = tknz.tokenize_text_by_enumerating()
unique_symbols = tknz.unique_symbols


def calculate_transition_matrix(text_digitized, markov_dim):
    prob_matrix = SparseMatrix([len(unique_symbols)] * (markov_dim + 1))
    for i in tqdm(range(markov_dim, len(text_digitized))):
        n_gram_and_char = tuple(text_digitized[i - markov_dim: i + 1])
        prob_matrix[n_gram_and_char] += 1
    return prob_matrix

prob_matrix = calculate_transition_matrix(text_digitized, markov_dim)


n_tokens_to_generate = 1500
chars_in_line = 100

a = np.random.randint(0, len(text_digitized) - markov_dim)
left = tuple(text_digitized[a: markov_dim + a])
print("Начинаем генерирование текста: ", left)
for i in range(n_tokens_to_generate):

    distr = np.array( [prob_matrix[(left + (x, ))] for x in range(0, prob_matrix.shape[0])])

    if not sum(distr): continue
    distr = distr / sum(distr)
    char = np.random.choice(range(prob_matrix.shape[0]), p=distr)
    print(unique_symbols[char], end=" " if tokens_are_words else "", flush=True)
    if i % 70 == 0: print()
    left = (left + (char,))[1:]


