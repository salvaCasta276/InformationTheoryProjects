import sys
sys.path.insert(0,"..")
import numpy as np
from Project1.HandIn1 import InfoTheory
from Project2.huffman_binary_tree import HuffmanBinaryTree
from tabulate import tabulate

with open('Alice29.txt', 'r') as file:
    rawChars = np.array([char for line in file for char in line])

chars, counts = np.unique(rawChars, return_counts=True)
char_count_dict = dict(zip(chars, counts))

totalChars = rawChars.size
charDistr = counts/totalChars

char_prob_dict = dict(zip(chars, charDistr))
sorted_char_prob_dict = dict(sorted(char_prob_dict.items(), key=lambda item: item[1]))
print(tabulate(sorted_char_prob_dict.items(), headers=['Char', 'Probability']))

hbt = HuffmanBinaryTree(sorted_char_prob_dict)
code_dict = hbt.get_codes()
print(tabulate(code_dict.items(), headers=['Char', 'Code']))

IT = InfoTheory()
entropy = IT.Entropy(np.array([charDistr]))
print(f"Entropy: {entropy[0]}")

avg = 0
for char in chars:
    avg += len(code_dict[char])*sorted_char_prob_dict[char]
print(f"Average word length: {avg}")

compressed_len = 0
for char in chars:
    compressed_len += len(code_dict[char])*char_count_dict[char]
print(f"Size of original file: {rawChars.size*8}")
print(f"Size of compressed file in bits: {compressed_len}")
