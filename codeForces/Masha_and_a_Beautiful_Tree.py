for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    def merge(left, right):
        global ans

        if left[0] <= right[0]:
            return left + right
        else:
            ans+=1
            return right + left
            
    
    def merge_sort(nums, s, e):
        if e ==s:
            return [nums[s]]
        
        m = s + (e-s)//2

        left = merge_sort(nums, s, m)
        right = merge_sort(nums, m+1, e)

        return merge(left, right)
    
    if sorted(arr) == merge_sort(arr, 0, n-1):

        print(ans)
    else:
        print(-1)