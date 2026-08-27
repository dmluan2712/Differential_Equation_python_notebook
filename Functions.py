import numpy as np
# This function check if the input is a prime number or not.
def is_prime(n):
    check = 1
    for k in range(2,int(np.sqrt(n)+1)):
        if n/k == int(n/k):
            check = 0
            break
    return(check)

def prime_factorization(n):
    answer = str(n) + " = " # convert n to a text
    p = 2 # starting prime factor we need to check if it divides n or not
    if (is_prime(n)==1):
        print ("%i is a prime number"%n)
        return # return nothing and stop the function right here

    while (n>1) and (p<=n):
        if (is_prime(p)==1) and (int(n/p)==(n/p)):
            n = n/p # n has new value which is itself divided by the factor p
                # the algorithm runs with this new value of n, until n=1
            answer = answer  + str(p) + " x "
        else:
            p = p + 1 # increase the value of p, regardless p divides or p is a prime or not  
    answer = answer[:-2] # remove the last "x " from the string 
    print(answer)

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    prime_factorization(n)        
