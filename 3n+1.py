import numpy as np
import timeit

def collatza(n): # 
    answer = str(n) + ", "
    while n != 1:
        if n % 2 == 0:
            n //= 2 
            answer += str(n) + ", "
        else:
            n = 3*n + 1
            answer += str(n) + ", "
    print(answer)

def collatzb(n): # recursive method
    output = [int(n)]   # an array with starting number 
    if n == 1:
        return output # nothing to do
    else: 
        if n % 2 == 0:
            output.extend(collatzb(n/2)) # the function calls itself inside its definition
            return output
        else:
            output.extend(collatzb(3*n+1))
            return output

if __name__=="__main__":
    n=int(input("Enter a positive integer: "))
    # time the process
    starta = timeit.timeit()
    collatza(n)
    enda = timeit.timeit()
    time_run_a = enda - starta
    print(f"Time run for method 1: {time_run_a}")

    startb = timeit.timeit()
    print(collatzb(n))
    endb = timeit.timeit()
    time_run_b = endb - startb  
    print(f"Time run for method 2: {time_run_b}")
