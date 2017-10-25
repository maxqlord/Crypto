import copy
def det_mod(m, mod):
    return (m[0][0]*m[1][1] - m[0][1]*m[1][0]) % mod
def det(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def scalar_mult_mod(m,s,mod):
    m2 = copy.deepcopy(m)
    m2[0][0] = (m2[0][0]*s) % mod
    m2[0][1] = (m2[0][1]*s) % mod
    m2[1][0] = (m2[1][0]*s) % mod
    m2[1][1] = (m2[1][1]*s) % mod
    return m2
def inv_mat(m,mod):
    
def matrix_mult_mod(m1,m2,mod):
    ans = []
    for row in range(len(m1)):
        ans.append([])
        for col in range(len(m2[0])):
            a = m1[row][0]*m2[0][col] + m1[row][1]*m2[1][col]
            a = a % mod
            ans[row].append(a)
    return ans
        
matrix = [[1,2],[5,19]]
print(det_mod(matrix, 26))
matrix2 = [[4,5],[20,4]]
print(scalar_mult_mod(matrix2, 3, 26))
matrix3 = [[2,3],[5,7]]
matrix4 = [[1,8],[2,1]]
print(matrix_mult_mod(matrix3, matrix4, 26))
matrix5 = [[5,3]]
matrix6 = [[2,9],[1,3]]
print(matrix_mult_mod(matrix5, matrix6, 26))
matrix7 = [[2,5],[1,7]]
matrix8 = [[5],[2]]
print(matrix_mult_mod(matrix7, matrix8, 26))

