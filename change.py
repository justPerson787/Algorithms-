# Uses python3
#TFind the minimum number of coins needed to change the input value (an integer) into coins 
# with denominations 1, 5, and 10. 
# Input Format. The input consists of a single integer m. 
# Constraints. 1 ≤ m ≤ 103. Output Format. 
# Output the minimum number of coins with denominations 1, 5, 10 that changes m.

import sys

def get_change(m):
    coins = [10, 5, 1]
    n = m//10 + (m % 10) // 5 + (m % 10) % 5
    #write your code here
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
