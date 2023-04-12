import sys
sys.path.insert(0,"..")

import numpy as np
from Project1.HandIn1 import InfoTheory


with open('Alice29.txt', 'r') as file:
    rawChars = np.array([char for line in file for char in line])

chars, counts = np.unique(rawChars, return_counts=True)
totalChars = rawChars.size
charDistr = counts/totalChars

IT = InfoTheory()
entropy = IT.Entropy(np.array([charDistr]))

print(charDistr)
print(entropy[0])
print(np.log2(chars.size))

charProbDict = dict(zip(chars, 1/counts))
