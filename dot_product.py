#Uses python3
#Task. Given two sequences a1,a2,...,an (ai is the profit per click of the i-th ad) and b1,b2,...,bn (bi is the average 
# number of clicks per day of the i-th slot), we need to partition them into n pairs (ai,bj) such that the sum of their 
# products is maximized. 
# Input Format. The first line contains an integer n, the second one contains a sequence of integers a1,a2,...,an, 
# the third one contains a sequence of integers b1,b2,...,bn. 
# Output Format. Output the maximum value of n ∑︀ i=1 aici, where c1,c2,...,cn is a permutation of b1,b2,...,bn.

import sys

def max_dot_product(a, b):    
    a.sort(reverse=True)
    b.sort(reverse=True)   
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

#for tests
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
