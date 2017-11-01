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
        return ''
    msg = prepare_string(msg, alpha)
    if len(msg) % 2 == 1:
        msg += "A"
    result = ''
    for i in range(0, len(msg), 2):
        matrix = matrix_mult_mod(bi2matrix(msg[i:i+2], alpha), inv, mod)
        result += matrix2bi(matrix, alpha)
    return result
        
def find_a(digraph1, digraph2, enc1, enc2, alpha):
    matrix1 = [[c2i(digraph1[0], alpha), c2i(digraph1[1], alpha)], [c2i(digraph2[0], alpha), c2i(digraph2[1], alpha)]]
    matrix2 = [[c2i(enc1[0], alpha), c2i(enc1[1], alpha)], [c2i(enc2[0], alpha), c2i(enc2[1], alpha)]]

    a = matrix_mult_mod(matrix_inverse_mod(matrix1, len(alpha)), matrix2, len(alpha))
    return a    

    
def hard_code_loop(encrypted, common, alpha):
    mod = len(alpha)
    #matrix = [[c2i(encrypted[0][1][0], alpha), c2i(encrypted[0][1][1], alpha)], [c2i(encrypted[1][1][0], alpha), c2i(encrypted[1][1][1], alpha)]]
    for a in range(0, mod):
        print("*********")
        for b in range(mod):
            print(b)
            for c in range(mod):
                print(c)
                for d in range(mod):
                    encrypt = [[a, b], [c, d]]
                    for user in encrypted:
                        if(matrix_2x2_encode(user[1], encrypt, alpha) in common):
                            print(encrypt)
                            break

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!.?0123456789-*"
'''
matrix = find_a("TO","ER","AQ","8J", alpha)                     
print(matrix_2x2_encode("M4468NZ.F0SR6*BD4GTOPKBV*1D7?TYSKDCXHG!EJ147SDL8SFFPG8O2R4NDJJXGG!.A66NMJ947.AZH-2BXIZ.*EM", matrix, alpha))
'''
matrix = [[7,24],[4,3]]
message = "RMPFXC8ED2I3X7B8CV-RE5OT.NJ0DN"
print(matrix_2x2_encode(message, matrix, alpha))
