import numpy as np
import itertools

#Function used to calculate values of the type G(1, m) where m is any value equal or greater than 1
#It can be proven that G(1, m) has dimensions (m+1)x(2^m), we use this to calculate the dimension of the 0 block
def G(r, m):
    if r > 1 or m < r:
        raise ValueError("r cannot be greater than 1 neither m can be smaller than r")

    if r == 0:
        return np.ones((2 ** m,))

    if r == m:
        return np.identity(2 ** m)

    top_matrix = G(r, m-1)
    return np.block([[top_matrix, top_matrix], [np.zeros((1, 2**(m-1))), G(r-1, m-1)]])


m = 3
generator = G(1, m)

bin = {0,1}
bin_power = itertools.product(bin, repeat=2**(m-1))
codewords = [np.dot(np.array(u), generator)%2 for u in bin_power]
for codeword in codewords:
    print(codeword)

errors = np.identity(2 ** m)
syndromes = np.dot(errors, generator.T)%2
codeword = generator[1]

print(generator)
print(np.dot(generator, generator.T) % 2)
print(syndromes)
#We get the syndrom which we can use to find the error and add it to the codeword
print(np.dot((codeword + errors[0]), generator.T)%2)
#Add the error to intermediate value
print(((codeword + errors[0]) + errors[0])%2)
