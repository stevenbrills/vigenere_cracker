##README

This program was created for recreation to break the Vigenere cipher challenge in the book "The Code Book" by Simon Singh.

- What is the Vigenere Cipher?
Yadayadayada

- How can you break the cipher/ How does the software work?

The length of the message is found and we look for repetitions of sequences of length greater than 4.
For each sequnce, locate the positions of occurance and the spacing between them
Find the common factor between the spacings which will give the possible length of the key
The poly-alphabetic substitution is broken into mono-alphabetic cipher groupings
A frewuency analysis of occurnace is then done
The frequency histogram so obtained for each mono-alphabetic cipher is then cycled and minimized against the plaintext frequency histogram
The shift that minimizes the SSD suggests the character for the key used