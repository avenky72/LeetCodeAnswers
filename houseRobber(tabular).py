class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == 0:
                nums[0] = nums[0]
            elif i == 1:
                nums[1] = max(nums[1], nums[0])
            else:
                nums[i] = max(nums[i-1], (nums[i]+nums[i-2]))
        #print(nums)
        return nums[len(nums)-1]
