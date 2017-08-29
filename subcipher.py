# subcipher.py
# implements basic substitution ciphers

def c2i(c, alphabet):
    '''returns the index of c in the string alphabet, starting at 0'''
    return alphabet.find(c)

def i2c(i, alphabet):
    '''returns the character at index i in alphabet'''
    return alphabet[i]

def prepare_string(s, alphabet, make_uppercase = True):
    '''converts to uppercase if make_uppercase is true
    removes characters from s not in alphabet
    returns new string'''
    if make_uppercase == True:
       s = s.upper()
    for char in s:
        if char not in alphabet:
            s.replace(char, "")
    s = s.replace(" ", "")
    return s

def caesar_shift_encode(plaintext, shift, alphabet):
    '''prepares plaintext and returns a new string shifted by shift, relative to alphabet'''
    prepared = prepare_string(plaintext, alphabet)
    new_string = ""
    for letter in prepared:
        char_index = c2i(letter, alphabet)
        new_char = i2c((char_index + shift) % 26, alphabet)
        new_string += new_char
    return new_string
    
def caesar_shift_decode(ciphertext, shift, alphabet):
    '''return the plaintext, shifted by shifted, relative to alphabet'''

def subst_validate(alpha1, alpha2):
    '''verify that alpha1 and alpha2 contain exactly the same letters,
    return boolean'''
    return sorted(list(alpha1)) == sorted(list(alpha2))

def substitution_cipher_encode(plaintext, alpha1, alpha2):
    '''prepares plaintext, validates the alphabets, and returns a
    ciphertext using alpha2 as the substitution cipher alphabet'''
    prepared = prepare_string(plaintext, alpha1)
    new_string = ""
    if subst_validate(alpha1, alpha2):
        for letter in prepared:
            new_char = i2c(c2i(letter, alpha1), alpha2)
            new_string += new_char
        return new_string
    return "Invalid alphabets"
        

def substitution_cipher_decode(ciphertext, alpha1, alpha2):
    '''return the plaintext, validates the alphabets, and returns a
    plaintext using alpha1 as the original alphabet'''
