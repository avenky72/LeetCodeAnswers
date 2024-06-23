class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            #temp = nums[m]
            
            # if nums[r] < nums[m] the min is in the right if nums[r] > nums[m] the min is in the left
            if nums[r] < nums[m]:
                l = m + 1

            elif nums[r] > nums[m]:
                r = m
            
        return nums[l]



        
