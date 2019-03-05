# Uses python3
#Given an integer n, find the last digit of the nth Fibonacci number Fn (that is, Fn mod 10). 
#The input consists of a single integer n. 
# Constraints. 0 ≤ n ≤ 107. 
# Output the last digit of Fn.

import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current % 10

#for tests
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
