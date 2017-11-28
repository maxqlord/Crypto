from random import randint
from primefac import factorint


def m_r(n,k):
    d = n-1
    s = 0
    while d % 2 == 0:
        s+=1
        d = d // 2
    for i in range(k):
        if m_r_trial(n,s,d) == False:
            return False
    return True

def m_r_trial(n,s,d):
    a = random.randint(1,n-1)
    if pow(a,d,n) == 1:
        return True
    x = pow(a,d,n)
    r = 0
    while r <= s-1:
        if x == n-1:
            return True
        r+=1
        x = pow(x,2,n)
    return False

def main():
    print(m_r(2**20 + 1,10))
    print(factorint(2**20 + 1))
    
