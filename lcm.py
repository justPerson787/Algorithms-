# Uses python3
#Task. Given two integers a and b, find their least common multiple. 
#Input Format. The two integers a and b are given in the same line separated by space. 
#Constraints. 1 ≤ a,b ≤ 2·109. 
# Output Format. Output the least common multiple of a and b.

import sys

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return (a // gcd(a, b))*b
            
#for tests
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

