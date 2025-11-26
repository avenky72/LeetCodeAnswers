class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        """
        Find the leftmost pivot index where the left sum and right sum are equal
        """

        # running sum to keep track of left and right sum so don't need to keep recalculating
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i
            else:
                left_sum += nums[i]

        return -1

        
        
