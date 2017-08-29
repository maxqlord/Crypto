# driver.py
# Tests subcipher.py

from subcipher import *

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = "my coffee tastes like covfefe"
codebet = "QWERTYUIOPLKJHGFDSAZXCVBNM"
plaintext = plaintext.upper()
shift = 10

print("\n---Testing substitution-------")
ciphertext = substitution_cipher_encode(plaintext, alphabet, codebet)
recovered_text = substitution_cipher_decode(ciphertext, alphabet, codebet)
print("Plaintext = %s" % plaintext)
print("Ciphertext =%s" % ciphertext)
print("Recovered text = %s" % recovered_text)

print("\n---Testing Caesar-------")
ciphertext = caesar_shift_encode(plaintext, shift, alphabet)
recovered_text = caesar_shift_decode(ciphertext, shift, alphabet)
print("Plaintext = %s" % plaintext)
print("Ciphertext =%s" % ciphertext)
print("Recovered text = %s" % recovered_text)
