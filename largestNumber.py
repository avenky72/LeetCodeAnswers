class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''sort_list = []
        for i in range(len(nums)):
            n = nums[i]
            first_digit = n
            while first_digit > 9:
                first_digit = first_digit // 10
            sort_list.append((first_digit, n))

        print(sort_list)'''
        num = list(map(str, nums))
        
        for i in range(len(num)):
            for j in range(i+1, len(nums)):
                if int(num[i] + num[j]) < int(num[j] + num[i]):
                    num[i], num[j] = num[j], num[i]
        
        result = ''.join(num)
        
        if result[0] == '0':
            return '0'
        
        return result
                
            
