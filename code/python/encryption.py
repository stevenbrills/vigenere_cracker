from random import sample
import random
import numpy as np
from copy import deepcopy
from operator import itemgetter
import string

vigenere_square = []
alphabet_english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Read in the source text
plain_text = open("../../source_plaintext/plain_text.txt","r")
text = plain_text.read()
text = text.translate(str.maketrans('', '', string.punctuation))
text = "".join(text.split())
text = text.upper()
plain_text.close()

print(len(text))

print('You should now pick your keyword.  It should be less than the length of the formatted plaintext message which is ', len(text), ' characters long.\n')
keyword = input("Enter the keyword you want to use for encryption: ")

#Creating a reference Vigenere Square

for i in range(len(alphabet_english)):
    vigenere_square.append(np.roll(np.array(alphabet_english),-i))

print(vigenere_square)

keyword_shifts = list(keyword)

st = set(keyword_shifts)
keyword_shifts = [i for i, e in enumerate(alphabet_english) if e in st]

encrypted_text = ""

for i in range(len(text)):
    encrypted_text = encrypted_text + vigenere_square[keyword_shifts[i%len(keyword)]][np.where(vigenere_square[0][:]==text[i])[0][0]]

print(encrypted_text)