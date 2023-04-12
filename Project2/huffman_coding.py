import sys
sys.path.insert(0,"..")

import numpy as np
from Project1.HandIn1 import InfoTheory
from Project2.huffman_binary_tree import HuffmanBinaryTree


with open('Alice29.txt', 'r') as file:
    rawChars = np.array([char for line in file for char in line])

chars, counts = np.unique(rawChars, return_counts=True)
char_count_dict = dict(zip(chars, counts))

totalChars = rawChars.size
charDistr = counts/totalChars

IT = InfoTheory()
entropy = IT.Entropy(np.array([charDistr]))


char_prob_dict = dict(zip(chars, charDistr))
sorted_char_prob_dict = dict(sorted(char_prob_dict.items(), key=lambda item: item[1]))
print(sorted_char_prob_dict)

hbt = HuffmanBinaryTree(sorted_char_prob_dict)
code_dict = hbt.get_codes()
print(code_dict)

avg = 0
for char in chars:
    avg += len(code_dict[char])*sorted_char_prob_dict[char]

compressed_len = 0
for char in chars:
    compressed_len += len(code_dict[char])*char_count_dict[char]

print(f"Entropy: {entropy[0]}")
print(f"Average word length: {avg}")
print(f"Upper bound of entropy: {np.log2(chars.size)}")
print(f"Size of compressed file in bits: {compressed_len}")
print(f"Size of uncompressed file: {rawChars.size*8}")
