# Uses python3
#The goal in this code problem is to check whether an input sequence contains a majority element. 
# Input Format. The first line contains an integer n, the next one contains a sequence of n 
# non-negative integers a0,a1,...,an−1. 
# Constraints. 1 ≤ n ≤ 105; 0 ≤ ai ≤ 109 for all 0 ≤ i < n. 
# Output Format. Output 1 if the sequence contains an element that appears strictly more than n/2 times, and 0 otherwise.

import sys

def get_majority_element(a, left, right):
    #case of a single number
    if left == right:
        return -1
    #case of two numbers in array
    if left + 1 == right:
        if a[left] == a[right]:
            return a[left]
        else: 
            return -1

    a.sort()
    
    count1 = 1
    for i in range(len(a)-1):                   
        if a[i] == a[i+1]:
            count1 +=1 
            if count1 > len(a)//2:
                return (count1)
        else:
        #reset count1
            count1 = 1
    
    return -1

#test
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
