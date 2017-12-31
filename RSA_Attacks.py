import random
#from primefac import factorint
import time


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


def pick_primes_diff(e, diff):
    prime_list = []
    start = random.randrange(2 ** (e - 1), 2 ** e)
    while len(prime_list) < 2:
        if start > 2 ** e:
            if len(prime_list) == 0:
                start = random.randrange(2 ** (e - 1), 2 ** e)
            else:
                start = random.randrange(start - diff, start + diff)
        if m_r(start, 10):
            if len(prime_list) == 0:
                prime_list.append(start)
                start = random.randrange(start - diff, start + diff)
            else:
                if abs(prime_list[0] - start) <= diff and prime_list[0] != start:
                    prime_list.append(start)
                else:
                    start = random.randrange(start - diff, start + diff)
        start += 1
    return prime_list

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


def make_m(p, q):
    return p * q


def totient_m(p, q):
    return (p - 1) * (q - 1)


def pick_e(m):
    e = 65537
    # while gcd(e,m) != 1:
    # e += 2
    return e


def find_factors(a, m):
    quotients = []
    while m % a != 1:
        temp = a
        quotients.append((m - (m % a)) // a)
        a = m % a
        m = temp
    quotients.append((m - (m % a)) // a)
    return quotients


def mod_eq(x, y, z, quotients, m):
    if z >= len(quotients):
        return y % m, x % m
    else:
        return mod_eq(y, y * -1 * quotients[z] + x, z + 1, quotients, m)


def solve_d(a, m):
    quotients = find_factors(a, m)
    quotients = quotients[::-1]
    return mod_eq(1, -quotients[0], 1, quotients, m)

def create_sequence(length, alpha):
    sequence = "<"
    for i in range(length-2):
        letter = random.choice(list(alpha))
        while letter == "<" or letter == ">":
            letter = random.choice(list(alpha))
        sequence += letter
    sequence += ">"
    return sequence
    
def convert_message(plaintext, alpha, m):
    for i in range(3):
        index = random.randint(0,len(plaintext))
        plaintext = plaintext[:index] + create_sequence(random.randint(4,20),alpha) + plaintext[index:] 
    power = 0
    while len(alpha) ** power < m:
        power += 1
    power -= 1
    x = len(plaintext) % power
    if x != 0:
        plaintext += create_sequence(power+power-x, alpha)

    print(plaintext)
    plain_array = []
    num_array = []
    for i in range(0, len(plaintext), power):
        plain_array.append(plaintext[i:i + power])
    # print(plain_array)
    i = power - 1
    for word in plain_array:

        converted_num = 0
        for char in word:
            index = c2i(char, alpha)
            converted_num += index * (len(alpha) ** i)
            i -= 1
        i = power - 1
        num_array.append(converted_num)

    return num_array


def encrypt_num(num, e, m):
    encrypt_list = []
    for element in range(len(num)):
        encrypt_list.append(pow(num[element], e, m))
    return encrypt_list


def decrypt_num(num, d, m):
    decrypt_list = []
    for element in range(len(num)):
        decrypt_list.append(pow(num[element], d, m))
    return decrypt_list

def remove_junk(message):
    while "<" in message:
        index = message.find("<")
        while message[index] != ">":
            message = message[:index] + message[index+1:]
        message = message[:index] + message[index+1:]
    return message

def convert_num(decrypted, alpha, m):
    power = 0
    while len(alpha) ** (power + 1) < m:
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
    print(message)
    message = remove_junk(message)
        
    return message

    
def main():
    alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ;:<>"
    plaintext = "My name is Maximus Decimus Meridius, Commander of the Armies of the North, General of the Felix Legions, loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
    m = 101533675266204711531654785393679402237996918671114485049619417758278007006594690108173215546012245481143359145312245046121095659949331214052351454912828387999134593248922700747814819913654302080371106303479499351344317982601786702908390357301888078578018864923801739786681821006546489694096357917919507186951
    e = 65537
    totient = 101533675266204711531654785393679402237996918671114485049619417758278007006594690108173215546012245481143359145312245046121095659949331214052351454912828367823172069714434695993745516329872565920722985195154349692291357325359114667779265264838546142869407734801731385038882151575625499763768473474594283095400
    d = 24905860255725879161128558371435831215619245076168217368168847519448208502647607278010781895992994161387622894243551754908566669657528550240407738974604099075717750167527536701335931161313935177709426888586620163469122180790593518153401412904839522602020213691084940505135564165734707633891419802212150312673
    num = convert_message(plaintext, alpha, m)
    encrypted = encrypt_num(num,e,m)
    print(encrypted)
    decrypted = decrypt_num(encrypted, d, m)
    print(decrypted)
    message = convert_num(decrypted, alpha, m)
    print(message)
    

main()
