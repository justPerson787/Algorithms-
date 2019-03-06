# Uses python3
# Given two integers a and b, find their greatest common divisor. 
# Input.The two integers a,b are given in the same line separated by space. 
# Constraints. 1 ≤ a,b ≤ 2·109.
# Output Format. Output GCD(a,b).

import sys

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
#for automatic tests    
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
