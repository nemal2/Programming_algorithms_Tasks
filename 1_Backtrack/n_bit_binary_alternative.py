def bitStr(n):
    if n==0: return []
    if n==1: return ["0", "1"]
    return [ digit + bitstring for digit in bitStr(1) 
            for bitstring in bitStr(n-1)]

print(bitStr(3))

# print([ digit + bitstring for digit in range(3) 
#              for bitstring in range(2)])