# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    price=[]       
    #calculate price per weight unit for each item
    for i in range (0, len(weights)):        
            price.append(values[i] / weights[i])
    #sort price and weights vectors from most valuable items to least valuable    
    price, weights = [list(x) for x in zip(*sorted(zip(price, weights), reverse=True, key=lambda pair: pair[0]))]
    while capacity > 0 and sum(weights) > 0:
        for i in range (0, len(price)):        
            value = value + min(capacity, weights[i])*price[i]
            capacity = capacity - min(capacity, weights[i])
            weights[i] = weights[i]- min(capacity, weights[i])
    
    return value

#for tests
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
