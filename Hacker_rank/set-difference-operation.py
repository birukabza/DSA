# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums1 = set(map(int, input().split()))
m = int(input())
nums2 = set(map(int, input().split()))

set_diff = nums1.difference(nums2)

print(len(set_diff))

