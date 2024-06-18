arr=["0","0","0"]
def bit(n):
    if n<1:
        print(arr)
    else:
        arr[n-1]="0"
        bit(n-1)
        arr[n-1]="1"
        bit(n-1)

bit(3)
