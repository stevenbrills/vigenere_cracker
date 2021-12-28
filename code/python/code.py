from random import sample
import numpy as np

#Load file
abc_freq = np.array([8.2, 1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,6.3,9.1,2.8,0.98,2.4,0.15,2,0.074])

#Read in the source text
source_text = open("../../source_text/cipher_text.txt","r")
text = source_text.read()
text = "".join(text.split())

print(len(text))

#program specifications and initializations
min_length = 4
max_length = 10
identified_count = 0
test_words = []
test_word_counts = []

# while identified_count<5:

#randomly pick a word length between 4 and some max limit
search_word_length = sample(range(min_length,max_length+1),1)[0]
print(search_word_length)

  
#randomly pick a word of that length from the text
sampling_set = [(text[i:i+search_word_length]) for i in range(0, len(text), search_word_length)]
search_word_sample = sample(sampling_set, 1)[0]
search_word_sample = "EEDC"
print(search_word_sample)


#check for repetitions and count the repetitions
num_repetitions = sampling_set.count(search_word_sample)
print(num_repetitions)

ind1 = text.index(search_word_sample,0)
ind2 = text.index(search_word_sample,ind1)

print(ind1)
print(ind2)


#if repetitions more than 1, save it else discard
if num_repetitions>1:
    test_words = [test_words, search_word_sample]
    test_word_counts = [test_word_counts, num_repetitions]


#loop again with a new word length and new word until we have a minimum number of repeated keywords

#using the space between repetitions and find all factors of the spacing

#extract the common factor, that becomes the length of the key

#split the text into mono-alphabetic ciphers and find the frequency distribution

#iterate and minimise the frequency wrt the standard frequency distribution

#predict the keyword and decode the message

