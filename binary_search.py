# Uses python3
# Implement the binary search algorithm. 
# Input Format. The first line of the input contains an integer n and a sequence a0 < a1 < ... < an−1 of n pairwise 
# distinct positive integers in increasing order. The next line contains an integer k and k positive 
# integers b0,b1,...,bk−1. 
# Constraints. 1 ≤ n,k ≤ 104; 1 ≤ ai ≤ 109 for all 0 ≤ i < n; 1 ≤ bj ≤ 109 for all 0 ≤ j < k;
# Output Format. For all i from 0 to k−1, output an index 0 ≤ j ≤ n−1 such that aj = bi or −1 if there is no such index.
import sys

def binary_search(a, x):
    #output=[]          
    #for i in range(len(a)):
    index=-1
    left, right = 0, len(a)-1
    mid = 0
    while left <= right:
        mid = left + (right - left)//2
        if x == a[mid]:
            index = mid
            break            
                
        else:
            if x < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return index

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

#tests
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
