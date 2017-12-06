import copy
from math import gcd


def c2i(c, alphabet):
    return alphabet.find(c)

def i2c(i, alphabet):
    return alphabet[i]

def bi2i(bi, alphabet):
    return c2i(bi[0], alphabet) * len(alphabet) + c2i(bi[1], alphabet)

def i2bi(i, alphabet):
    mod = len(alphabet)
    second = i % mod
    first = int((i-second) / mod)
    #print(first)
    #print(second)
    return i2c(first, alphabet) + i2c(second, alphabet)

def inv_mod(a, m):
    for i in range(m):
        if(a*i) % m == 1:
            return i
    return None

def det_mod(m, mod):
    return (m[0][0] * m[1][1] - m[0][1] * m[1][0]) % mod

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

        
def find_a(digraph1, digraph2, enc1, enc2, alpha):
    matrix1 = [[c2i(digraph1[0], alpha), c2i(digraph1[1], alpha)], [c2i(digraph2[0], alpha), c2i(digraph2[1], alpha)]]
    matrix2 = [[c2i(enc1[0], alpha), c2i(enc1[1], alpha)], [c2i(enc2[0], alpha), c2i(enc2[1], alpha)]]

    a = matrix_mult_mod(matrix_inverse_mod(matrix1, len(alpha)), matrix2, len(alpha))
    return a

def coefficients(plaintext, ciphertext, alpha):
    for a in range(0, 500):
        for b in range(0,500):
            if(affine_encode(plaintext, alpha, a, b) == ciphertext):
                return a,b
    return -1

def affine_encode(text, alpha, a, b):
    #test coprime
    mod = len(alpha)
    if gcd(a, mod) != 1:
        return None
    
    ciphertext = ""
    for char in text:
        index = c2i(char, alpha)
        encoded_num = (a*index + b) % mod
        encoded_char = i2c(encoded_num, alpha)
        ciphertext += encoded_char
    return ciphertext

def affine_decode(text, alpha, a, b):
    mod = len(alpha)
    plaintext = ""
    for char in text:
        encoded_index = c2i(char, alpha)
        decoded_index = ((encoded_index + mod - b) * inv_mod(a, mod)) % mod
        decoded_char = i2c(decoded_index, alpha)
        plaintext += decoded_char
    return plaintext
def table():
    print("Alphabet size\t" + "A values possible\t" + "B values possible\t" + "Total transformations")
    for i in range(20, 61):
        a = find_a_values(i)
        print(str(i) + "\t\t" + str(a) + "\t\t\t" + str(i) + "\t\t\t" + str(a*i))
def find_a_values(mod):
    counter = 0
    for i in range(1, mod):
        if gcd(i,mod) == 1:
            counter += 1
    return counter
def affine_bigraph_encode(text, alpha, a, b):
    mod = len(alpha)
    if gcd(a, mod) != 1:
        return None
    if len(text) % 2 == 1:
        text += "X"
    ciphertext = ""
    for i in range(0, len(text), 2):
        bigraph = text[i] + text[i+1]
        encoded_num = (a * bi2i(bigraph, alpha) + b) % (mod*mod)
        ciphertext += i2bi(encoded_num, alpha)

    return ciphertext
               
def affine_bigraph_decode(text, alpha, a, b):
    mod = len(alpha)*len(alpha)
    plaintext = ""
    for i in range(0, len(text), 2):
        bigraph = text[i] + text[i+1]
        encoded_index = bi2i(bigraph, alpha)
        decoded_index = ((encoded_index + mod - b) * inv_mod(a, mod)) % mod
        decoded_bi = i2bi(decoded_index, alpha)
        plaintext += decoded_bi
    return plaintext
def equation_solve(a,b):
    return np.linalg.solve(a,b)

#finds transformation coefficients given encoding
def bigraph_coefficients(plaintext, ciphertext, alpha):
    for a in range(0, 500):
        for b in range(0,500):
            if(affine_bigraph_encode(plaintext, alpha, a, b) == ciphertext):
                return a,b
    return -1

def bi2matrix(bi, alpha):
    return [[c2i(bi[0], alpha), c2i(bi[1], alpha)]]

def matrix_2x2_encode(msg, matrix, alpha):
    mod = len(alpha)
    if len(msg) % 2 == 1:
        msg += "A"
    '''
    inv = matrix_inverse_mod(matrix, mod)
    if inv == None:
        print("Returned none")
        return ''
    '''
    #msg = prepare_string(msg, alpha)
    
    result = ''
    for i in range(0, len(msg), 2):
        matrix2 = matrix_mult_mod(bi2matrix(msg[i:i+2], alpha), matrix, mod)
        result += matrix2bi(matrix2, alpha)
    return result

def find_matrix(plain, enc, alpha):
    plain_text = plain[0:4]
    enc_text = enc[0:4]
    plain_matrix = [[c2i(plain_text[0],alpha), c2i(plain_text[1],alpha)], [c2i(plain_text[2],alpha), c2i(plain_text[3],alpha)]]
    enc_matrix = [[c2i(enc_text[0],alpha), c2i(enc_text[1],alpha)], [c2i(enc_text[2],alpha), c2i(enc_text[3],alpha)]]
    print(plain_matrix)
    print(enc_matrix)
    mod = len(alpha)
    inv_matrix = matrix_inverse_mod(plain_matrix, mod)
    if inv_matrix == None:
        return None
    return matrix_mult_mod(inv_matrix, enc_matrix, mod)

def find_matrix2(plain, enc, alpha):
    for a in range(0, len(alpha)):
        print(a)
        for b in range(0, len(alpha)):
            for c in range(0, len(alpha)):
                for d in range(0, len(alpha)):
                    matrix = [[a,b],[c,d]]
                    if matrix_2x2_encode(plain, matrix, alpha) == enc:
                        print(matrix)
                        print(matrix_inverse_mod(matrix, len(alpha)))


''' affine works
alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ;:"
plaintext = "Whenyoucontrolthemailyoucontrolinformation!"
print(affine_bigraph_encode(plaintext, alpha, 476,1929))

ciphertext = "VJtImogkDNOCzNVNzk,;,aS?qmwNB;TaNNy,rvMaRuQQlNQWSIPs"
print(affine_bigraph_decode(ciphertext, alpha, 476,1929))
'''


alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;-,!"
matrix = [[33,4],[31,30]]
plaintext = "Youwouldnteatbroccoliifitwasdeepfriedinchocolate!"
print(matrix_2x2_encode(plaintext, matrix, alpha))

ciphertext = "eQaJgyiDxuTrkOBbRAhFjpaItodpxMCEjpVhPlhodi.qcrCEgyWxefJlnHPlWyEgLfPlmyGbzYhIRhKiiDmqiDxuHJhuVSBuXujYcrWQbucYC-yEYdxNdihIPFUoMegqUGWjsLuUGKWxaQcrHHiUOA"
inv = matrix_inverse_mod(matrix, len(alpha))
print(matrix_2x2_encode(ciphertext, inv, alpha))

m2 = [[5, 52], [15, 38]]
m3 = [[38, 14], [15, 14]]

print(matrix_2x2_encode("Seinfeld", m3, alpha))
print(matrix_2x2_encode("kbmXU.Fk", m3, alpha))
print(matrix_2x2_encode("kbmXU.Fk", m2, alpha))





'''matrix = find_matrix("Seinfeld", "kbmXU.Fk", alpha)
print(matrix)
'''
find_matrix2("Seinfeld", "kbmXU.Fk", alpha)
print("first one")















#matrix = [[33,4],[31,30]]
#message = "eQaJgyiDxuTrkOBbRAhFjpaItodpxMCEjpVhPlhodi.qcrCEgyWxefJlnHPlWyEgLfPlmyGbzYhIRhKiiDmqiDxuHJhuVSBuXujYcrWQbucYC-yEYdxNdihIPFUoMegqUGWjsLuUGKWxaQcrHHiUOA"
#print(matrix_2x2_encode(message, matrix_inverse_mod(matrix, 57), alpha))
#print(affine_bigraph_decode(ciphertext, alpha, 476, 1929))

'''
matrix = find_a("TO","ER","AQ","8J", alpha)                     
print(matrix_2x2_encode("M4468NZ.F0SR6*BD4GTOPKBV*1D7?TYSKDCXHG!EJ147SDL8SFFPG8O2R4NDJJXGG!.A66NMJ947.AZH-2BXIZ.*EM", matrix, alpha))

matrix = [[7,24],[4,3]]
message = "RMPFXC8ED2I3X7B8CV-RE5OT.NJ0DN"
print(matrix_2x2_encode(message, matrix, alpha))
'''
