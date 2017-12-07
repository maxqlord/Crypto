from math import gcd
import random

def c2i(c, alphabet):
    return alphabet.find(c)

def i2c(i, alphabet):
    return alphabet[i]

def m_r_trial(n, s, d):
    a = random.randint(1, n - 1)
    if pow(a, d, n) == 1:
        return True
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    x = pow(a, d, n)
    r = 0
    while r <= s - 1:
        if x == n - 1:
            return True
        r += 1
        x = pow(x, 2, n)
    return False

def m_r(n, k):
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d = d // 2
    for i in range(k):
        if not m_r_trial(n, s, d):
            return False
    return True

def pick_primes(e):
    prime_list = []
    start = random.randrange(2 ** (e - 1), 2 ** e)
    while len(prime_list) < 2:
        if start >= 2 ** e:
            start = random.randrange(2 ** (e - 1), 2 ** e)

        if m_r(start, 10):
            prime_list.append(start)
            start = random.randrange(2 ** e - 1, 2 ** e)
        start += 1
    return prime_list

def make_m(p,q):
    return p*q

def totient_m(p,q):
    return (p-1)*(q-1)

def pick_e(m):
    e = 65537
    while gcd(e,m) != 1:
        e += 2
    return e

def solve_d(e, m, totient): #change
    for d in range(m):
        if (e * d) % totient == 1:
            return d
    return None

def convert_message(plaintext, alpha, m):
    power = 0
    while len(alpha) ** power < m:
        power += 1
    power -= 1
    converted_num = 0
    for char in plaintext:
        index = c2i(char, alpha)
        converted_num += index * len(alpha) ** power
        power -= 1
    return converted_num

def encrypt_num(num, e, m):
    return (num ** e) % m

def decrypt_num(num, d, m):
    return (num ** d) % m

def convert_num(decrypted, alpha, m):
    message = ""
    while decrypted > 0: #?
        message += i2c(decrypted % len(alpha), alpha)
        decrypted //= len(alpha)
    return message
                           

def main():
    alpha = "1ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = "TEST"
    p = pick_primes(10)
    m = make_m(p[0],p[1])
    totient = totient_m(p[0],p[1])
    e = pick_e(m)
    d = solve_d(e,m,totient)
    num = convert_message(plaintext, alpha, m)
    encrypted = encrypt_num(num,e,m)
    decrypted = decrypt_num(encrypted, d, m)
    message = convert_num(decrypted, alpha, m)
    print(p)
    print(m)
    print(totient)
    print(e)
    print(d)
    print(num)
    print(encrypted)
    print(decrypted)
    print(message)
    

main()
    
    
