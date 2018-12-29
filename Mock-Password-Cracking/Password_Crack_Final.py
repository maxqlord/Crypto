import copy, time

def c2i(c, alphabet='!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]'):
    return alphabet.find(c)

def i2c(i, alphabet='!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]'):
    return alphabet[i:i+1]

def det_mod(m, mod):
    return (m[0][0] * m[1][1] - m[0][1] * m[1][0]) % mod

def inv_mod(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def bi2matrix(bi, alpha):
    return [[c2i(bi[0], alpha), c2i(bi[1], alpha)]]

def matrix2bi(matrix, bi):
    return i2c(matrix[0][0], alpha) + i2c(matrix[0][1], alpha)

def scalar_mult_mod(m, s, mod):
    m2 = copy.deepcopy(m)
   
    for x in range(len(m)):
        for y in range(2):
            m2[x][y] = (m2[x][y] * s) % mod
    return m2

def matrix_mult_mod(m1, m2, mod):

    ans = []
  
    for row in range(len(m1)):
        ans.append([])
        for col in range(len(m2[0])):
            a = (m1[row][0] * m2[0][col] + m1[row][1] * m2[1][col]) % mod
            ans[row].append(a)
    return ans

def matrix_inverse_mod(m1, mod):
    d = det_mod(m1, mod)
    inv = inv_mod(d, mod)
    if inv == None:
        return None
    m2 = [[m1[1][1], -1 * m1[0][1]], [-1 * m1[1][0], m1[0][0]]]
    return scalar_mult_mod(m2, inv, mod)

def prepare_string(s, alphabet, make_uppercase = True):
    if make_uppercase:
        s = s.upper()
    s = s.replace(" ", "")
    for char in s:
        if char not in alphabet:
            s = s.replace(char, '')
    return s

def matrix_2x2_encode(msg, matrix, alpha):
    mod = len(alpha)
    inv = matrix_inverse_mod(matrix, mod)
    if inv == None:
        return None
    msg = prepare_string(msg, alpha)
    if len(msg) % 2 == 1:
        msg += "A"
    result = ''
    for i in range(0, len(msg), 2):
        matrix = matrix_mult_mod(bi2matrix(msg[i:i+2], alpha), inv, mod)
        #print(matrix)
        result += matrix2bi(matrix, alpha)
    return result

def find_matrix(plain, enc, alpha):
    plain_text = plain[0:4]
    enc_text = enc[0:4]
    plain_matrix = [[c2i(plain_text[0]), c2i(plain_text[1])], [c2i(plain_text[2]), c2i(plain_text[3])]]
    enc_matrix = [[c2i(enc_text[0]), c2i(enc_text[1])], [c2i(enc_text[2]), c2i(enc_text[3])]]
    mod = len(alpha)
    inv_matrix = matrix_inverse_mod(plain_matrix, mod)
    if inv_matrix == None:
        return None
    return matrix_mult_mod(inv_matrix, enc_matrix, mod)
def hard_code_loop(encrypted, common, alpha):
    
    mod = len(alpha)
    for user in encrypted:
        for word in common:

            matrix = find_matrix(word, user[1], alpha)
            if matrix == None:
                continue

            if matrix_2x2_encode(user[1][0:len(word)], matrix, alpha) == word:
                print(user)
                print(matrix_2x2_encode(user[1], matrix, alpha), word)
                return matrix

start = time.time()
encrypted_passwords = []
encrypted = open("encrypted.txt","r")
for line in encrypted.readlines():
      line = line.strip()
      (w1,w2) = line.split()
      encrypted_passwords.append([w1,w2])
encrypted.close()

common_words = []
common = open("common.txt","r")
for line in common.readlines():
      line = line.strip()
      common_words.append(line.upper())
common.close()

common_words = [x for x in common_words if len(x) > 6 and any(char.isdigit() for char in x) == False]
alpha = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]'

#print(common_words)
#print(encrypted_passwords)
m = hard_code_loop(encrypted_passwords, common_words, alpha)
print("*****")
print(m)
print("***")
f = open('helloworld.txt','w')
for user in encrypted_passwords:
    f.write(matrix_2x2_encode(user[1], m, alpha) + "\n")
f.close()
print('time: ', time.time() - start)
