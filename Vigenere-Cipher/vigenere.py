# vigenere.py
from collections import Counter
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

def index_of_coincidence(ciphertext, alpha):
    c = Counter(ciphertext)
    sum_probs = 0
    for char in alpha:
        sum_probs += c[char] * (c[char] - 1)
    return sum_probs/(len(ciphertext) * (len(ciphertext)-1))

def friedman_test(ciphertext, alpha):
    I = index_of_coincidence(ciphertext, alpha)
    n = len(ciphertext) #length of full message
    l = (.027 * n)/(.0655 - I + (n*(I-.0385))) #estimated keyword length
    return l
    
    

def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(vigenere_encode("THISISATEST", "KEY", alpha))
    print(vigenere_decode("KIBHGFFMSTIJUIVL", "CIPHER", alpha))
    
    std_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751, .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]
    random = sum([x**2 for x in std_freq])
    
    print(random)
    print(index_of_coincidence("UZRZEGNJENVLISEXRHLYPYEGTESBJHJCSBPTGDYFXXBHEEIFTCCHVRKPNHWXPCTUQTGDJHTBIPRFEMJCNHVTCFSAIIJENREGSALHXHWZWRZXGTTVWGDHTEYXISAGQTCJPRSIAPTUMGZALHXHHSOHPWCZLBRZTCBRGHCDIQIKTOAAEFTOPYEGTENRAIALNRXLPCEPYKGPNGPRQPIAKWXDCBZXGPDNRWXEIFZXGJLVOXAJTUEMBLNLQHGPWVPEQPIAXATYENVYJEUEI",alpha))
    print(friedman_test("UZRZEGNJENVLISEXRHLYPYEGTESBJHJCSBPTGDYFXXBHEEIFTCCHVRKPNHWXPCTUQTGDJHTBIPRFEMJCNHVTCFSAIIJENREGSALHXHWZWRZXGTTVWGDHTEYXISAGQTCJPRSIAPTUMGZALHXHHSOHPWCZLBRZTCBRGHCDIQIKTOAAEFTOPYEGTENRAIALNRXLPCEPYKGPNGPRQPIAKWXDCBZXGPDNRWXEIFZXGJLVOXAJTUEMBLNLQHGPWVPEQPIAXATYENVYJEUEI",alpha))
main()
