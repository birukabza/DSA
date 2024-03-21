if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    i = 0
    for _ in range(n):
        if i<n-1 and arr[i] == arr[i+1]:
            i+=1
    print(arr[i+1])
        
