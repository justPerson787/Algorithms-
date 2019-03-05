# Uses python3
# Given an integer n, find the nth Fibonacci number Fn. The input consists of a single integer n. 
# Constraints. 0 ≤ n ≤ 45. Output Format: Output Fn.

def calc_fib(n):
    if (n <= 1):
        return n

    fib = [0, 1]
    while len(fib) <= n:
        k  = fib[len(fib)-1]+fib[len(fib)-2]
        fib.append(k)
    return fib[len(fib)-1]

#for automatic test    
n = int(input())
print(calc_fib(n))
