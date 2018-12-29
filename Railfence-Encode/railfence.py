#railfence.py

def prepare_string(s, alphabet, make_uppercase = True):
    if make_uppercase == True:
       s = s.upper()
    for char in s:
        if char not in alphabet:
            s.replace(char, '')
    s.replace(' ','')
    s = ''.join(s.split())
    return s


def railfence_encode(plaintext, alpha):
    top = []
    middle = []
    bottom = []
    ciphertext = ""
    plaintext = prepare_string(plaintext, alpha)
    if(len(plaintext) > 3):
        for i in range(0, len(plaintext), 4):
            top.append(plaintext[i])
        for j in range(1, len(plaintext), 2):
            middle.append(plaintext[j])
        for k in range(2, len(plaintext), 4):
            bottom.append(plaintext[k])
        ciphertext += ''.join(top) + ''.join(middle) + ''.join(bottom)
        return ciphertext
    return plaintext

    

def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(railfence_encode("HELLOWORLD", alpha))
main()
