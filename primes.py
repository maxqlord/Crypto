from timeit import default_timer as timer
from random import randint

def primecheck(n, check):
    for prime in check: #for each prime number less than sqrt n
        if n % prime == 0:
            return False
    return True

def find_primes(n):
    found_primes_list = [] #list to be returned
    primes_to_check = primes_list(int((2**n+1)**.5)) #create primes list- up to the sqrt of biggest possible random num
    for i in range(0,10):
        number = randint(2**n,2**(n+1)) + 1 #starting number
        while(primecheck(number,primes_to_check) == False): #while current number is not prime
            number+=1
        found_primes_list.append(number)
    return found_primes_list

def primes_list(n):
    primes = []
    all_nums = [True] * (n+1)
    for i in range(2, n+1): #index
        if all_nums[i]:
            primes.append(i)
            for j in range(i, n+1, i): #cuts out all multiples of 
                all_nums[j] = False
    return primes


start = timer()
primes_list = find_primes(40) 
stop = timer()

print(stop - start)
print(primes_list) 
