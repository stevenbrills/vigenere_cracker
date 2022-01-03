from random import sample
import random
import numpy as np
from copy import deepcopy
from operator import itemgetter

#Load file


#Read in the source text
source_text = open("../../source_text/cipher_text.txt","r")
text = source_text.read()
text = "".join(text.split())
text = text.upper()
source_text.close()

print(len(text))

#program specifications and initializations
abc_standard_freq = np.array([8.2, 1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,6.3,9.1,2.8,0.98,2.4,0.15,2,0.074])
alphabet_english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
min_length = 4                  #Minimum length of search word
max_length = 10                 #Maximum length of search word
test_word_count = 0             #Count of number of repeating words
test_words = []                 #Saved list of search words with more than 1 occurance
test_word_occurances = []       #Saved list of number of occurances corresponding to each search word
repetition_gaps = np.array([])  #Gaps between each occurance
flag_stop = 0                   #Flag to keep trying searches, 0--> Keep searching, 1--> Stop and decode
number_of_cf = 0                #Number of common factors
mono_alphabetic_cipher_text_splits = []   #Contains the individual monoalphaetic cipher texts
vigenere_square = []            #Initializing a reference Vigenere Square
are_you_happy = 0               #Flag to check if user is satisfied with decryption

#Creating a reference Vigenere Square
for i in range(len(alphabet_english)):
    vigenere_square.append(np.roll(np.array(alphabet_english),-i))

print(vigenere_square)

#Loop until user is satisfied with decryption
while True:
        
    # loop that keeps trying the search based on flag_stop
    while flag_stop != 1:

        # break

        #Resetting things that have to be reset
        number_of_cf = 0

        #randomly pick a word length between min length and some max length
        search_word_length = sample(range(min_length,max_length+1),1)[0]
        print("Length of Search Word Is: ",search_word_length)

        
        #randomly pick a word of that length from the text
        random_start_index = random.randint(0,len(text))
        print("Random Starting Index: ", random_start_index)
        search_word_sample = text[random_start_index:random_start_index+int(search_word_length)]

        # print(len(search_word_sample))

        if len(search_word_sample) != search_word_length:
            continue

        #delete later
        #search_word_sample = "EEDC"
        print("Random Search Word Sample: ",search_word_sample)


        #check for repetitions and count the repetitions
        num_repetitions = text.count(search_word_sample)
        print("Number of Repetitions of Search Word: ", num_repetitions)

        #if repetitions more than 1 save it, else discard
        if num_repetitions>1:
            test_words = [test_words, search_word_sample]
            test_word_occurances = [test_word_occurances, num_repetitions]
            test_word_count += 1
        else:
            continue

        prev_index_of_occurance = text.index(search_word_sample,0)
        print(prev_index_of_occurance)

        #Find the character gaps between each occurance and store them


        for i in range(num_repetitions-1):
            index_of_occurance = text.index(search_word_sample, prev_index_of_occurance+1)
            print(index_of_occurance)
            # print(repetition_gaps.shape)
            # print(np.array(index_of_occurance).reshape(1,).shape)
            repetition_gaps = np.concatenate((repetition_gaps,np.array(index_of_occurance - prev_index_of_occurance).reshape(1,)))
            repetition_gaps = repetition_gaps.astype(int)
            print(repetition_gaps.dtype)
            prev_index_of_occurance = index_of_occurance


        #Make a copy of the list of gaps for factorization
        repetition_gaps_factorization = deepcopy(repetition_gaps)


        #Loop and find the number of common factors between the different character gaps
        while np.gcd.reduce(repetition_gaps_factorization) != 1:
            common_factor = np.gcd.reduce(repetition_gaps_factorization)
            number_of_cf += 1
            repetition_gaps_factorization = repetition_gaps_factorization/common_factor
            repetition_gaps_factorization = repetition_gaps_factorization.astype(int)

        #Change flag if we have found unique common factor with more than two repeated search words
        if number_of_cf == 1 and test_word_count > 2:
            flag_stop = 1
        
        print(common_factor)

    #extract the common factor, that becomes the length of the key
    length_of_key = common_factor

    #split the text into mono-alphabetic ciphers
    mono_alphabetic_cipher = ""
    mono_alphabetic_cipher_text_splits = []

    for i in range(length_of_key):
        for j in range(i,len(text),10):
            mono_alphabetic_cipher = mono_alphabetic_cipher + text[j]
        mono_alphabetic_cipher_text_splits.append(mono_alphabetic_cipher)
        mono_alphabetic_cipher = ""

    #find frequency distriution for each cipher texts
    frequency_dist = np.empty((length_of_key,26))
    shift_for_each_mono = []

    for i in range(len(mono_alphabetic_cipher_text_splits)):
        for j in range(len(alphabet_english)):
            frequency_dist[i,j] = (mono_alphabetic_cipher_text_splits[i].count(alphabet_english[j],0)/len(mono_alphabetic_cipher_text_splits[i]))*100

        min_ssd_val = np.linalg.norm(abc_standard_freq - frequency_dist[i])
        ssd_val = np.linalg.norm(abc_standard_freq - frequency_dist[i])
        correct_shift = 0
        shift = 0

        for k in range(len(alphabet_english)):
            ssd_val = np.linalg.norm(np.roll(abc_standard_freq,k) - frequency_dist[i])
            shift = k

            if ssd_val < min_ssd_val:
                min_ssd_val = ssd_val
                correct_shift = shift
        
        shift_for_each_mono.append(correct_shift)

    print(shift_for_each_mono)

    #Find the keyword
    keyword = list(itemgetter(*shift_for_each_mono)(alphabet_english))
    print(keyword)

    #decode message using the keyword
    decoded_text = ""

    for i in range(len(text)):
        # print(vigenere_square[shift_for_each_mono[i%len(keyword)]])
        # print(np.where(vigenere_square[shift_for_each_mono[i%len(keyword)]]==text[i])[0][0])
        # print(vigenere_square[0][np.where(vigenere_square[shift_for_each_mono[i%len(keyword)]]==text[i])[0]])
        decoded_text = decoded_text + vigenere_square[0][np.where(vigenere_square[shift_for_each_mono[i%len(keyword)]]==text[i])[0][0]]

    print(decoded_text)

    flag_stop = 0
    are_you_happy = int(input("Are you satisfied with the decryption? (Enter 0 for No or 1 for Yes): "))
    # print(are_you_happy)

    if are_you_happy == 1:
        break