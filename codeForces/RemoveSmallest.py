def solve():
    n = int(input())
    arr = list(map(int, (input().split())))
    arr.sort()
    diff =None
    
    for i in range(n-1):
        diff = arr[i+1]-arr[i]
        if diff>1:
            return "No"
        else:
            pass
    return "Yes"
    
t = int(input())
for _ in range(t):
    print(solve())


            
        