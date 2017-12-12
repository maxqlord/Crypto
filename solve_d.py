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
        print(x,y,z)
        return mod_eq(y, y*-1*quotients[z] + x, z+1, quotients, m)

def solve_d(a,m):
    quotients = find_factors(a,m)
    quotients = quotients[::-1]
    print(quotients)
    return mod_eq(1,-quotients[0], 1, quotients, m)

def main():
    print(mod_inv(85,331))

main()
