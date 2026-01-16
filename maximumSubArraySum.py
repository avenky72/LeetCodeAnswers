class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr = 0 
        max_sum = float('-inf')

        for i in nums:
            """if (i + curr) < 0:
                curr = 0
            else:
                curr += i"""
            curr = max(i, curr + i)
            
            max_sum = max(curr, max_sum)
        
        return max_sum
            
            
        
