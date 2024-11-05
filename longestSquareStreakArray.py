import math
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        arr = set(nums)
        long_seq = 0
        streak = 0
        prev = 0
        
        for num in nums:
            if num in arr:  
                streak = 0
                current = num
                
                while current in arr:
                    streak += 1
                    arr.remove(current) 
                    current = current ** 2
                
                long_seq = max(long_seq, streak)
        
        return long_seq if long_seq > 1 else -1
