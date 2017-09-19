# subcipher.py
# implements basic substitution ciphers
from collections import Counter

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
            s.replace(char, '')
    s.replace(' ','')
    s = ''.join(s.split())
    return s

def caesar_shift_encode(plaintext, shift, alphabet):
    '''prepares plaintext and returns a new string shifted by shift, relative to alphabet'''
    prepared = prepare_string(plaintext, alphabet)
    new_string = ""
    for letter in prepared:
        char_index = c2i(letter, alphabet)
        new_char = i2c((char_index + shift) % len(alphabet), alphabet)
        new_string += new_char
    return new_string
    
def caesar_shift_decode(ciphertext, shift, alphabet):
    '''return the plaintext, shifted by shifted, relative to alphabet'''
    new_string = ""
    for letter in ciphertext:
        char_index = c2i(letter, alphabet)
        new_char_index = char_index - shift
        if(new_char_index < 0):
            new_char_index += len(alphabet)
        new_char = i2c(new_char_index, alphabet)
        new_string += new_char
    return new_string

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
    '''prepares plaintext, validates the alphabets, and returns a
    plaintext using alpha1 as the original alphabet'''
    new_string = ""
    if subst_validate(alpha1, alpha2):
        for letter in ciphertext:
            new_string+=i2c(c2i(letter, alpha2),alpha1)
    return new_string

def create_keyword_alpha(keyword, alphabet_source):
    keyword_reduced = ''.join(sorted(set(keyword), key=keyword.index)).upper()
    new_alpha = list(alphabet_source)
    for letter in keyword_reduced:
        if letter in new_alpha:
            new_alpha.remove(letter)
    new_alpha = ''.join(new_alpha)
    new_alpha = keyword_reduced + new_alpha
    return new_alpha

def keyword_substitution_cipher_encode(plaintext, keyword, alphabet_source):
    ''' return a string encoding 'plaintext' using a keyword
    subst. cipher with 'keyword' as the keyword and 'alphabet_source'
    as the source alphabet. The string 'plaintext' is prepared first
    by capitalizing and removing spaces. '''
    new_alpha = create_keyword_alpha(keyword, alphabet_source)
    prepared_plain = prepare_string(plaintext, alphabet_source)
    return substitution_cipher_encode(prepared_plain, alphabet_source, new_alpha)

def keyword_substitution_cipher_decode(ciphertext, keyword, alphabet_source):
    ''' return a string decoding ciphertext using a keyword'''
    new_alpha = create_keyword_alpha(keyword, alphabet_source)
    prepared_cipher = prepare_string(ciphertext, alphabet_source)
    return substitution_cipher_decode(prepared_cipher, alphabet_source, new_alpha)

def letter_frequencies(text, alphabet, freq_number): #freq_number = number of common letters returned
    prepared_text = prepare_string(text, alphabet)
    c = Counter(prepared_text)
    return c.most_common(freq_number) #number of letter frequencies returned
    
def digraph_frequencies(text, alphabet, freq_number):
    prepared_text = prepare_string(text, alphabet)
    digraph_list = []
    for i,j in enumerate(prepared_text):
        digraph = prepared_text[i:i+2]
        if len(digraph) == 2:
            digraph_list.append(digraph)
    c = Counter(digraph_list)
    return c.most_common(freq_number)

def trigraph_frequencies(text, alphabet, freq_number):
    prepared_text = prepare_string(text, alphabet)
    trigraph_list = []
    for i,j in enumerate(prepared_text):
        trigraph = prepared_text[i:i+3]
        if len(trigraph) == 3:
            trigraph_list.append(trigraph)
    c = Counter(trigraph_list)
    return c.most_common(freq_number)
    
def double_letter_frequencies(text, alphabet, freq_number):
    prepared_text = prepare_string(text, alphabet)
    double_letter_list = []
    for i,j in enumerate(prepared_text):
        digraph = prepared_text[i:i+2]
        if len(digraph) == 2:
            if digraph[0] == digraph[1]:
                double_letter_list.append(digraph)
    c = Counter(double_letter_list)
    return c.most_common(freq_number)

def all_frequencies(text, alphabet, freq_number):
    return letter_frequencies(text, alphabet, freq_number), digraph_frequencies(text, alphabet, freq_number), trigraph_frequencies(text, alphabet, freq_number), double_letter_frequencies(text, alphabet, freq_number)
