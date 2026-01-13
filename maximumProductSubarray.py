class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_max = nums[0]
        # used to keep track of negative values generally
        prev_min = nums[0]
        output = nums[0]

        for i in range(1, len(nums)):
            temp_max = prev_max
            temp_min = prev_min
            prev_max = max(nums[i], nums[i] * temp_max, nums[i] * temp_min)
            prev_min = min(nums[i], nums[i] * temp_max, nums[i] * temp_min)
            output = max(output, prev_max)
        
        return output
