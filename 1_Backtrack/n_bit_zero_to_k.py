def range_to_list(k):
    res = []
    for i in range(0,k):
        res.append(str(i))
    return res

def bitStr(n,k):
    if n==0: return []
    if n==1: return range_to_list(k)
    return [ digit + bitstring for digit in bitStr(1,k) 
            for bitstring in bitStr(n-1,k)]

print(bitStr(5,5))
