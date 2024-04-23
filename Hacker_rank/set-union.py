# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums1 = set(map(int, input().split()))
m = int(input())
nums2 = set(map(int, input().split()))

print(len(nums1.union(nums2)))
