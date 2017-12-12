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

def find_factors(a,m):
    quotients = []
    while m % a != 1:
        temp = a
        quotients.append((m- (m % a))//a)
        a = m % a
        m = temp
    quotients.append((m- (m % a))//a)
    return quotients

def mod_eq(x,y, z, quotients,m):
    if z >= len(quotients):
        return y % m
    else:
        return mod_eq(y, y*-1*quotients[z] + x, z+1, quotients, m)

def solve_d(a,m):
    quotients = find_factors(a,m)
    quotients = quotients[::-1]
    return mod_eq(1,-quotients[0], 1, quotients, m)   
    

def convert_message(plaintext, alpha, m):
    power = 0
    while len(alpha) ** power < m:
        power += 1
    power -= 1
    while len(plaintext) % power != 0:
        plaintext+="Z"

    plain_array = []
    num_array = []
    for i in range(0,len(plaintext),power):
        plain_array.append(plaintext[i:i+power])
    print(plain_array)
    i = power - 1
    for word in plain_array:
        
        converted_num = 0
        for char in word:
            index = c2i(char, alpha)
            converted_num += index * (len(alpha) ** i)
            i -= 1
        i = power-1
        num_array.append(converted_num)
        
    return num_array

def encrypt_num(num, e, m):
    encrypt_list = []
    for element in range(len(num)):
        encrypt_list.append(pow(num[element],e,m))
    return encrypt_list

def decrypt_num(num, d, m):
    decrypt_list = []
    for element in range(len(num)):
        decrypt_list.append(pow(num[element],d,m))
    return decrypt_list

def convert_num(decrypted, alpha, m):

    power = 0
    while len(alpha) ** (power+1) < m:
        power += 1
    message = ""
    for element in range(0, len(decrypted)):
        num = decrypted[element]
        string_section = ""
        for x in range(power):
            n = num % len(alpha)
            string_section += i2c(n, alpha)
            num -= n
            num //= len(alpha)
        message += string_section[::-1]
    return message
                           
#need to rewrite convert_num and solve_d
def main():
    #modinv(85,331)
    p = pick_primes(511)
    m = make_m(p[0],p[1])
    totient = totient_m(p[0],p[1])
    e = pick_e(m)
    d = solve_d(e, totient)
    print(d)
    ''' 
    alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;-, !'"
    plaintext = "This is a sentence with completely normal formatting and as you can see as long as you include every character in your alphabet, it will decode perfectly with no issues whatsoever, isn't that exciting!"
    
    #p = pick_primes(10)
    m = make_m(10745914002293,14627728288231)
    totient = totient_m(10745914002293,14627728288231)
    print(m)
    print(totient)
    e = pick_e(m)
    num = convert_message(plaintext, alpha, m)
    print(num)
    encrypted = encrypt_num(num,e,m)
    print(encrypted)
    d = 100987439193303955497674873#solve_d(e,m,totient)
    print(d)
    decrypted = decrypt_num(encrypted, d, m)
    print(decrypted)
    message = convert_num(decrypted, alpha, m)
    print(message)
    '''


main()
    
    
