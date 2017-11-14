import copy


def c2i(c, alphabet):
    return alphabet.find(c)

def i2c(i, alphabet):
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
        
def find_a(digraph1, digraph2, enc1, enc2, alpha):
    matrix1 = [[c2i(digraph1[0], alpha), c2i(digraph1[1], alpha)], [c2i(digraph2[0], alpha), c2i(digraph2[1], alpha)]]
    matrix2 = [[c2i(enc1[0], alpha), c2i(enc1[1], alpha)], [c2i(enc2[0], alpha), c2i(enc2[1], alpha)]]
    inv = matrix_inverse_mod(matrix1, len(alpha))
    if(inv == None):
        return None
    a = matrix_mult_mod(inv, matrix2, len(alpha))
    return a

'''ideas
for each user
    for each word
        take first bigraph of user password and word and find necessary encryption matrix to make it work
        check second bigraph
            if works print if not move to next word
'''




def hard_code_loop(encrypted, common, alpha):
    m_list = []
    mod = len(alpha)
    #matrix = [[c2i(encrypted[0][1][0], alpha), c2i(encrypted[0][1][1], alpha)], [c2i(encrypted[1][1][0], alpha), c2i(encrypted[1][1][1], alpha)]]
    for user in encrypted:
        #print(user)
        for word in common:
            #print(word)
            wordcrib1 = word[0:2]
            pwordcrib1 = user[1][0:2]
            wordcrib2 = word[2:4]
            pwordcrib2 = user[1][2:4]
            wordcrib3 = word[4:6]
            pwordcrib3 = user[1][4:6]
            #print(wordcrib1, wordcrib2, pwordcrib1, pwordcrib2)
            m = find_a(wordcrib1, wordcrib2, pwordcrib1, pwordcrib2, alpha)
            m2 = find_a(wordcrib1, wordcrib3, pwordcrib1, pwordcrib3, alpha)
            m3 = find_a(wordcrib2, wordcrib3, pwordcrib2, pwordcrib3, alpha)
            if m != None and m2 != None and m3 != None and m == m2 == m3 and m not in m_list:  #test rest of word
                m_list.append(m)
    return m_list



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
print(m)
#test(encrypted_passwords, common_words, alpha, m)
