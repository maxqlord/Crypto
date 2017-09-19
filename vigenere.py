# vigenere.py
def c2i(c, alphabet):
    return alphabet.find(c)

def i2c(i, alphabet):
    return alphabet[i]

def prepare_string(s, alphabet, make_uppercase = True):
    if make_uppercase == True:
       s = s.upper()
    for char in s:
        if char not in alphabet:
            s.replace(char, '')
    s.replace(' ','')
    s = ''.join(s.split())
    return s

def vigenere_encode(plaintext, key, alpha):
    ciphertext = ""
    key_index = 0
    plaintext = prepare_string(plaintext, alpha)
    key = prepare_string(key, alpha)
    for letter in plaintext:
        if key_index >= len(key):
            key_index = 0
        coded_index = (c2i(letter, alpha) + c2i(key[key_index], alpha)) % 26
        ciphertext += i2c(coded_index, alpha)
        key_index+=1
    return ciphertext

def vigenere_decode(ciphertext, key, alpha):
    plaintext = ""
    key_index = 0
    ciphertext = prepare_string(ciphertext, alpha)
    key = prepare_string(key, alpha)
    for letter in ciphertext:
        if key_index >= len(key):
            key_index = 0
        coded_index = (c2i(letter, alpha) - c2i(key[key_index], alpha)) % 26
        plaintext += i2c(coded_index, alpha)
        key_index+=1
    return plaintext
def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(vigenere_encode("THISISATEST", "KEY", alpha))
    print(vigenere_decode("KIBHGFFMSTIJUIVL", "CIPHER", alpha))
main()
