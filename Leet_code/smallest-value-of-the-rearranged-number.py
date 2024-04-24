class Solution:
    def smallestNumber(self, num: int) -> int:
        isNegative  = False
        if num < 0:
            isNegative = True
        
        num_list = list(map(int, str(abs(num))))
        
        if isNegative:
            num_list.sort(reverse = True)
            return -int("".join([str(n) for n in num_list]))
        else:
            num_list.sort()
            if num_list[0] == 0:
                for i in range(len(num_list)):
                    if num_list[i]!=0:
                        num_list[0], num_list[i] = num_list[i], num_list[0]
                        break
            return int("".join([str(n) for n in num_list]))
        