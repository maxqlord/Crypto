#affine.py
from math import gcd
import numpy as np

def c2i(c, alphabet):
    return alphabet.find(c)

def i2c(i, alphabet):
    return alphabet[i]

def bi2i(bi, alphabet):
    return c2i(bi[0], alphabet) * len(alphabet) + c2i(bi[1], alphabet)

def i2bi(i, alphabet):
    mod = len(alphabet)
    second = i % mod
    first = int((i-second) / mod)
    #print(first)
    #print(second)
    return i2c(first, alphabet) + i2c(second, alphabet)

def inv_mod(a, m):
    for i in range(m):
        if(a*i) % m == 1:
            return i
    return None

def affine_encode(text, alpha, a, b):
    #test coprime
    mod = len(alpha)
    if gcd(a, mod) != 1:
        return None
    
    ciphertext = ""
    for char in text:
        index = c2i(char, alpha)
        encoded_num = (a*index + b) % mod
        encoded_char = i2c(encoded_num, alpha)
        ciphertext += encoded_char
    return ciphertext

def affine_decode(text, alpha, a, b):
    mod = len(alpha)
    plaintext = ""
    for char in text:
        encoded_index = c2i(char, alpha)
        decoded_index = ((encoded_index + mod - b) * inv_mod(a, mod)) % mod
        decoded_char = i2c(decoded_index, alpha)
        plaintext += decoded_char
    return plaintext
def table():
    print("Alphabet size\t" + "A values possible\t" + "B values possible\t" + "Total transformations")
    for i in range(20, 61):
        a = find_a_values(i)
        print(str(i) + "\t\t" + str(a) + "\t\t\t" + str(i) + "\t\t\t" + str(a*i))
def find_a_values(mod):
    counter = 0
    for i in range(1, mod):
        if gcd(i,mod) == 1:
            counter += 1
    return counter
def affine_bigraph_encode(text, alpha, a, b):
    mod = len(alpha)
    if gcd(a, mod) != 1:
        return None
    if len(text) % 2 == 1:
        text += "X"
    ciphertext = ""
    for i in range(0, len(text), 2):
        bigraph = text[i] + text[i+1]
        encoded_num = (a * bi2i(bigraph, alpha) + b) % (mod*mod)
        ciphertext += i2bi(encoded_num, alpha)

    return ciphertext
               
def affine_bigraph_decode(text, alpha, a, b):
    mod = len(alpha)*len(alpha)
    plaintext = ""
    for i in range(0, len(text), 2):
        bigraph = text[i] + text[i+1]
        encoded_index = bi2i(bigraph, alpha)
        decoded_index = ((encoded_index + mod - b) * inv_mod(a, mod)) % mod
        decoded_bi = i2bi(decoded_index, alpha)
        plaintext += decoded_bi
    return plaintext
def equation_solve(a,b):
    return np.linalg.solve(a,b)
#finds transformation coefficients given encoding
def bigraph_coefficients(plaintext, ciphertext, alpha):
    for a in range(0, 500):
        for b in range(0,500):
            if(affine_bigraph_encode(plaintext, alpha, a, b) == ciphertext):
                return a,b
    return -1
def coefficients(plaintext, ciphertext, alpha):
    for a in range(0, 500):
        for b in range(0,500):
            if(affine_encode(plaintext, alpha, a, b) == ciphertext):
                return a,b
    return -1

    
def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(affine_decode("FYGTGXKVYNPEPSXGLIEDQYWJLEIGWCQYTHQJQCPYLWPYCHQDY", alpha, 11, 6))
    print(affine_decode("SXQAHKWCEKYTBKTFFQWGBTESOHVYASSTKDSOXVBQHNHQYYHUSXTBQYKXV", alpha, 21, 10))
    print(affine_decode("XEIACKZMPOWBYTYWYVOFTYTERYWXABKPAUYRGTPOUBARGKQM", alpha, 9, 4))
    print(affine_bigraph_encode("BOMBOGENESIS", alpha, 375, 114))
    print(affine_bigraph_decode("SSPXYOPX", alpha, 343, 31))
    print(bigraph_coefficients("EARLYDECISION","SWAPQNWQOUHGJF",alpha))
    print(inv_mod(13,41))
    #HEANALYZEDPOPULARMOVIESFROMASCIENTIFICPERSPECTIVE
    #ONECLAIMWASTHATBBEIGHTWOULDSCOOTAROUNDHELPLESSLYONTHESAND
    #FAMOUSLYHECRITICIZEDTITANICFORSHOWINGTHEWRONGSKY
    text = "K7EP?G0MJLYO?!D0GW6KMUBQ*-.FJ-"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!.?0123456789-*" 
    print(affine_decode(text, alpha, 3, 0))
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(coefficients("FIREWORKS","FKZMQUZWS",alpha))
    
    
main()
