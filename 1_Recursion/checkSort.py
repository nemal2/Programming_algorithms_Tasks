def isSort(A):
    #Base case
    if len(A)==1:
        return True
    else:
        return A[0] <= A[1] and isSort(A[1:])
    
A=[1,2,3,4,7,13,12]
print(isSort(A))