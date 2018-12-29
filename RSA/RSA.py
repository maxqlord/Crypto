from math import gcd
import random

def c2i(c, alphabet):
    return alphabet.find(c)

def prepare_string(s, alphabet):

    for char in s:
        if char not in alphabet:
            s.replace(char, '')
    s.replace(' ','')
    s = ''.join(s.split())
    print(s)
    return s


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
    print(power)
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
                           

def main():
    #2082181,1761583
    #p = pick_primes(511)  #pick primes between 2^511 and 2^512
    p = [12146506381645834038938637694315560145605522481099001678525961130513503330983463286913894837422547560452046476688310536561557005074571465528726771144222297, 6841181471228144056720961233011919562929461148315947269150349289240990263876119140774193696991680295609812474830147505476097737728291793488537259523362993]
    eckel_mod = 2494279923802253606287472092668310204875649561581672691813431640440219048972006082731965879
    m = make_m(p[0],p[1]) #multiply
    totient = totient_m(p[0],p[1]) #calculate totient from primes
    e = 65537 #exponent
    d = solve_d(e, totient) #calculate d
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ., []0123456789"
    encrypted1 = [27529222289130396982441972178167156131188390270854605803088482820364727777356806293149110424664547444829506048862681707047361447940307458528855188797640951349314273871265869613531475173199205446725064541554710160734703958937428787702631909934402384936987117450673463038491985907253183292938459387572382618320]
    encrypted2 = [51067169418462057946035271407596584206898470229948837025243238360682207489049940521332316064501444037312305552752324515016504618449765390427754168876074131879784613096721414049832244807553779598060039598331370583030202390206371995360432749375936016189125266198408794541779708034026032700137396253674599089757]
    decrypted1 = decrypt_num(encrypted1, d, m)
    decrypted2 = decrypt_num(encrypted2, d, m)
    print(decrypted1)
    print(decrypted2)
    message1 = convert_num(decrypted1, alpha, m)
    message2 = convert_num(decrypted2, alpha, m)
    print(message1)
    print(message2)
    signature1 = [129348710293561219045692384213098475065291837410293856104574368752354612394871029586108276]
    signature2 = [786455771834685379588950282669850118588542062416352994035757229411495455300397962388489222]
    decodedsig1 = decrypt_num(signature1, e, eckel_mod)
    decodedsig2 = decrypt_num(signature2, e, eckel_mod)
    messagesig1 = convert_num(decodedsig1, alpha, eckel_mod)
    messagesig2 = convert_num(decodedsig2, alpha, eckel_mod)
    print(messagesig1)
    print(messagesig2)
    


main()
