class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr = 0
        max_sum = float('-inf')

        for i in nums:
            curr += i
            max_sum = max(curr, max_sum)
            
            if curr < 0:
                curr = 0
                
        return max_sum
        

