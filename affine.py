#affine.py
from math import gcd

def c2i(c, alphabet):
    return alphabet.find(c)

def i2c(i, alphabet):
    return alphabet[i]

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

def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(affine_encode("ANEXAMPLE", alpha, 7, 8))
    print(affine_encode("ANYTHING", alpha, 13, 2))
    print(affine_decode("IVKNIOJHK", alpha, 7, 8))
    
main()
