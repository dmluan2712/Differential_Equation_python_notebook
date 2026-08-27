import numpy as np
import timeit

def collatza(n):
    answer = str(n) + ", "
    while n != 1:
        if n % 2 == 0:
            n //= 2 
            answer += str(n) + ", "
        else:
            n = 3*n + 1
            answer += str(n) + ", "
    print(answer)

if __name__=="__main__":
    n=int(input("Enter a positive integer: "))
    # time the process
    starta = timeit.timeit()
    collatza(n)
    enda = timeit.timeit()
    time_run = starta - enda
    print(f"Time run: {time_run}")
