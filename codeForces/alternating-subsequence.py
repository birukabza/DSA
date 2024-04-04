def sign(x: int):
    if x<0:
        return -1
    else:
        return 1

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    i = 0
    
    while i < n:
        j = i+1
        max_num = arr[i]
        
        while j < n and sign(arr[i]) == sign(arr[j]):
            max_num = max(max_num, arr[j])
            j+=1
        
        res+=max_num
        i = j
    
    return res

t = int(input())

for _ in range(t):
    print(solve())





        