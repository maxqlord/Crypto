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


def pick_primes(e, diff):
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
        sequence.append(random.choice(list(alpha)))
    sequence.append(">")
    return sequence
    
def convert_message(plaintext, alpha, m):
    power = 0
    while len(alpha) ** power < m:
        power += 1
    power -= 1
    while len(plaintext) % power != 0:
        plaintext += " "

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

    message = remove_junk(message)
        
    
    return message

    
def main():

    '''alpha= "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;:-, !'0123456789"
    m=106382053895550781631285989946671994901422402885384005734669390130404880949239142241842903713130115581490732292356870236631337904281854676807813263510001411983900084040159377605552511174634634036897745619667852912154300017597144357866633696471699967965565310764085206116047453528193353554423244052263729215021
    print(solve_d(65537, 65539))
    '''
    
    '''
    alpha= "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;:-, !'0123456789"
    users = ["meckel","Meckel","mEckel", "MEckel", "mceckel","Mceckel","mCeckel", "mcEckel", "MCeckel", "McEckel", "MCEckel", "mCEckel", "malcom.eckel", "Malcom.eckel",  "malcom.Eckel",  "Malcom.Eckel"]
    m = 90487058565911344860746920532714345107344888706603388689414973118770115868824428038927974148369533060365472446789821522968583861289788613738073758712025234963231865997137994675667715748727317358600691229070201161969867856640249424928418473804035245009947964183514868695116591835621822263433693274598400210107
    e=65537
    intercepted = 1146948390450508061237246402938932791716411473847224475062235553042635385039708473826626084916757574374873906074434396951057457722800514748803933741138291677248905061102227147826086956521739130434782608695652173913043478260869565217391304347826086956521739130434782608695652173913043478260869565217391304347
    #print(intercepted)
    
    common_words = []
    common = open("common.txt","r")
    for line in common.readlines():
        line = line.strip()
        common_words.append(line)
    common.close()
    #print(common_words)
    for user in users:
        for password in common_words:
            if convert_message("userid:"+user+", password:" + password, alpha, m)[0] == intercepted:
                print(user)
                print(password)
                break
    '''

    

    

main()
