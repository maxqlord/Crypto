from primefac import *
import random
import time
import math


def perfect_square(n):
    if n == 1:
        return True
    low = 0
    high = n // 2
    root = high
    while root * root != n:
        root = (low + high) // 2
        if low + 1 >= high:
            return False
        if root * root > n:
            high = root
        else:
            low = root
    return True


def factor(n):
    x = int(math.ceil(n ** .5))
    while x < n:
        y2 = (x ** 2) - n
        if perfect_square(y2):
            y = int(y2 ** .5)
            factor1 = x + y
            factor2 = x - y
            return factor1, factor2
        x += 1


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
        if start > 2**e:
            if len(prime_list) == 0:
                start = random.randrange(2 ** (e - 1), 2 ** e)
            else:
                start = random.randrange(start-diff, start + diff)
        if m_r(start, 10):
            if len(prime_list) == 0:
                prime_list.append(start)
                start = random.randrange(start-diff, start + diff)
            else:
                if abs(prime_list[0]-start) <= diff and prime_list[0] - start != 0:
                    prime_list.append(start)
                else:
                    start = random.randrange(start-diff, start + diff)
        start += 1
    return prime_list


def run_multiple_trials(e):
    prime_time_list = []
    factor_time_list = []
    for x in range(10):

        prime_start = time.time()
        prime_list = []
        start = random.randrange(2 ** (e - 1), 2 ** e)
        while len(prime_list) < 2:
            if start >= 2 ** e:
                start = random.randrange(2 ** (e - 1), 2 ** e)

            if m_r(start, 10):
                prime_list.append(start)
                start = random.randrange(2 ** e - 1, 2 ** e)
            start += 1

        prime_end = time.time()
        prime_time_list.append(prime_end - prime_start)
        n = prime_list[0] * prime_list[1]
        factor_start = time.time()
        factors = factor(n)
        # factors = factorint(n);
        factor_end = time.time()
        factor_time_list.append(factor_end - factor_start)
    print("Average time to find two primes: " + str(sum(prime_time_list) / len(prime_time_list)))
    print("Average time to factor product: " + str(sum(factor_time_list) / len(factor_time_list)))


def run_trial(e):
    prime_start = time.time()
    prime_list = []
    start = random.randrange(2 ** (e - 1), 2 ** e)
    while len(prime_list) < 2:
        if start >= 2 ** e:
            start = random.randrange(2 ** (e - 1), 2 ** e)

        if m_r(start, 10):
            prime_list.append(start)
            start = random.randrange(2 ** e - 1, 2 ** e)
        start += 1

    prime_end = time.time()
    prime_time = prime_end - prime_start
    n = prime_list[0] * prime_list[1]
    factor_start = time.time()
    factors = factor(n)
    # factors = factorint(n);
    factor_end = time.time()
    factor_time = factor_end - factor_start

    print("Between 2 to the " + str(e - 1) + "th and 2 to the " + str(e) + "th power")
    print("Found primes " + str(prime_list[0]) + " and " + str(prime_list[1]))
    print("Product " + str(n))
    print("Factored to " + str(factors))
    print("Finding primes took " + str(prime_time) + " seconds")
    print("Factoring product took " + str(factor_time) + " seconds")


def run_multiple_trials_primefac(e):
    prime_time_list = []
    factor_time_list = []
    for x in range(10):

        prime_start = time.time()
        prime_list = []
        # start = random.randrange(2 ** (e - 1), 2 ** e)

        while len(prime_list) < 2:
            y = random.randint(2 ** (e - 1), 2 ** e)
            x = nextprime(y)
            if m_r(x, 10):
                prime_list.append(x)

        prime_end = time.time()
        prime_time_list.append(prime_end - prime_start)
        n = prime_list[0] * prime_list[1]
        factor_start = time.time()
        # factors = factor(n)
        factors = factorint(n);
        factor_end = time.time()
        factor_time_list.append(factor_end - factor_start)
    print("Average time to find two primes: " + str(sum(prime_time_list) / len(prime_time_list)))
    print("Average time to factor product: " + str(sum(factor_time_list) / len(factor_time_list)))


def run_trial_primefac(e):
    prime_start = time.time()
    prime_list = []

    while len(prime_list) < 2:
        y = random.randint(2 ** (e - 1), 2 ** e)
        x = nextprime(y)
        if m_r(x, 10):
            prime_list.append(x)

    prime_end = time.time()
    prime_time = prime_end - prime_start
    n = prime_list[0] * prime_list[1]
    factor_start = time.time()
    # factors = factor(n)
    factors = factorint(n);
    factor_end = time.time()
    factor_time = factor_end - factor_start

    print("Between 2 to the " + str(e - 1) + "th and 2 to the " + str(e) + "th power")
    print("Found primes " + str(prime_list[0]) + " and " + str(prime_list[1]))
    print("Product " + str(n))
    print("Factored to " + str(factors))
    print("Finding primes took " + str(prime_time) + " seconds")
    print("Factoring product took " + str(factor_time) + " seconds")


def main():
    """
    print(m_r(2 ** 20 + 1, 10))
    print(factorint(2 ** 20 + 1))
    run_multiple_trials_primefac(40) #40: .001025, 1.2444
    """
    arr = pick_primes(511, 10**2)
    print(arr)
    n = arr[0] * arr[1]
    print(n)
    print(arr[0] - arr[1])
    factor_start = time.time()
    print(factorint(n))
    factor_end = time.time()
    factor_time = factor_end - factor_start
    print(factor_time)


main()
